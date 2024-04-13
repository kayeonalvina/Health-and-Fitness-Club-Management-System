import customInput
import dbConnection
import member

def roomAvailable(connection, room, event):
    query = f"SELECT * FROM Events NATURAL JOIN MemberEvents WHERE room = '{room}' AND date = '{event['date']}' AND start_time = '{event['start_time']}'"
    result = dbConnection.executeSelectQuery(connection, query)

    if result:
        print("Room is not available at that time.")
        return False

    return True

def canPay(connection, memberID, amount):
    query = f"SELECT balance FROM Members WHERE member_id = '{memberID}'"
    result = dbConnection.executeSelectQuery(connection, query, False)

    if result["balance"] < amount:
        print("Insufficient funds.")
        return False

    return True

#Checks to see if changes in defective equipment will still allow for the events to take place
def equipmentAvailable(connection, equipmentID, newMax):
    query = f"SELECT * FROM MemberEvents NATURAL JOIN EquipmentUsage WHERE equipment_id = '{equipmentID}'"
    events = dbConnection.executeSelectQuery(connection, query)

    equipmentUsage = {}

    for event in events:
        equipmentUsage[(event['day_of_week'], event['start_time'])] = equipmentUsage.setdefault((event['day_of_week'], event['start_time']), 0) + event['num_in_use']
        if(equipmentUsage[(event['day_of_week'], event['start_time'])] > newMax):
            print("Equipment is not available at that time. Unable to perform action.")
            return False
        
    return True

def adminSession(connection):
    print("What would you like to do?")

    while True:
        print("1. Manage room bookings")
        print("2. Manage equipment")
        print("3. Update schedule")
        print("4. Process payments")
        print("0. Log out")

        choice = int(customInput.inputFormatted())

        if choice == 0:
            print("Logging out.")
            break

        elif choice == 1:
            print("Here are the current events:")

            query = "SELECT * FROM Events NATURAL JOIN MemberEvents"
            result = dbConnection.executeSelectQuery(connection, query)

            member.printSchedule(connection, result)

            noRoomIDs = []

            for event in result:
                if not event["room"]:
                    noRoomIDs.append(event["event_id"])
                
            print(f"NOTE: Events number {','.join(noRoomIDs)} do not have a room assigned to them.")

            while True:
                print("Which event would you like to assign a room to?(-1 to cancel)")
                eventID = int(customInput.inputFormatted())

                if eventID == -1:
                    print("Cancelling.")
                    break

                if eventID < 1 or eventID > len(result):
                    print("Invalid event ID. Please try again.")
                    continue

                print("Enter the new room number:")
                room = customInput.inputFormatted()

                if(roomAvailable(connection, room, result[eventID - 1])):
                    query = f"UPDATE Events SET room = '{room}' WHERE event_id = '{result[eventID - 1]['event_id']}'"
                    dbConnection.executeQuery(connection, query)
                    print("Room assigned.")

        elif choice == 2:
            allEquipment = dbConnection.executeSelectQuery(connection, "SELECT * FROM Equipment")

            while True:
                print("All equipment:")
                equipmentID = 1

                for equipment in allEquipment:
                    print(f"ID #{equipmentID}: {equipment['label']} - {equipment['total_quantity']} in stock, {equipment['defective_count']} defective")
                    equipmentID += 1

                print("Select an equipment ID to mark as maintain (-1 to cancel):")
                equipmentID = int(customInput.inputFormatted())

                if equipmentID == -1:
                    print("Cancelling.")
                    break

                if equipmentID < 1 or equipmentID > len(allEquipment):
                    print("Invalid equipment ID. Please try again.")
                    continue

                print("Enter the quantity to mark as defective. \nAlternatively, you can enter a negative number to mark defective equipment no longer defective:")
                quantity = int(customInput.inputFormatted())

                if(0 > allEquipment[equipmentID - 1]["defective_count"] - quantity or allEquipment[equipmentID - 1]["defective_count"] - quantity > allEquipment[equipmentID - 1]["total_quantity"]):
                    print("Input is out of bounds, assuming maximum possible value.")

                    if quantity > 0:
                        if(not equipmentAvailable(connection, equipmentID, allEquipment[equipmentID - 1]["total_quantity"] - allEquipment[equipmentID - 1]["defective_count"] - quantity)):
                            continue
                        quantity = allEquipment[equipmentID - 1]["total_quantity"] - allEquipment[equipmentID - 1]["defective_count"]
                        print(f"Marking {quantity} equipment as defective.")

                    else:
                        quantity = -allEquipment[equipmentID - 1]["defective_count"]
                        print(f"Marking {quantity} equipment as not defective.")
                
                query = f"UPDATE Equipment SET defective_count = defective_count - {quantity} WHERE equipment_id = '{allEquipment[equipmentID - 1]['equipment_id']}'"
                dbConnection.executeQuery(connection, query)
                print("Equipment updated.")
            
        elif choice == 3:
            weekSchedule = dbConnection.executeSelectQuery(connection, "SELECT * FROM Events NATURAL JOIN MemberEvents")

            while True:
                print("Weekly events:")
                member.printSchedule(connection, weekSchedule)

                print("Select an event ID to update the schedule for (-1 to cancel):")

                eventID = int(customInput.inputFormatted())

                if eventID == -1:
                    print("Cancelling.")
                    break

                if eventID < 1 or eventID > len(weekSchedule):
                    print("Invalid event ID. Please try again.")
                    continue
                    
                print("Enter the new day of week:")
                day = customInput.inputFormatted()

                print("Enter the new start time. Note that each event is 1 hour long:")
                start_time = customInput.inputFormatted()

                if(roomAvailable(connection, weekSchedule[eventID - 1]["room"], {"date": weekSchedule[eventID - 1]["date"], "start_time": start_time})):
                    query = f"UPDATE MemberEvents SET day_of_week = '{day}', start_time = '{start_time}' WHERE event_id = '{weekSchedule[eventID - 1]['event_id']}'"
                    dbConnection.executeQuery(connection, query)
                    print("Schedule updated.")

        elif choice == 4:
            allMembers = dbConnection.executeSelectQuery(connection, "SELECT * FROM Members NATURAL JOIN People")

            while True:
                print("All members:")
                memberID = 1

                for member in allMembers:
                    print(f"ID #{memberID}: {member['first_name']} {member['last_name']}: {member['balance']}")
                    memberID += 1
                
                print("Select a member ID to process a payment for (-1 to cancel):")
                memberID = int(customInput.inputFormatted())

                if memberID == -1:
                    print("Cancelling.")
                    break

                if memberID < 1 or memberID > len(allMembers):
                    print("Invalid member ID. Please try again.")
                    continue

                print("Enter the amount to pay:")
                amount = customInput.inputFormatted()

                if(canPay(connection, allMembers[memberID - 1]["member_id"], amount)):
                    query = f"UPDATE Members SET balance = balance - {amount} WHERE member_id = '{allMembers[memberID - 1]['member_id']}'"
                    dbConnection.executeQuery(connection, query)
                    print("Payment processed.")

        else:
            print("Invalid input. Please try again.")
        
        print()
