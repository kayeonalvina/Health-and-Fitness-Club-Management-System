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
                
            print(f"NOTE: Events number {",".join(noRoomIDs)} do not have a room assigned to them.")

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
            print("What would you like to do?")

            while True:
                print("1. Manage defective equipment")
                print("2. Update equipment for an event")
                print("0. Go back")

                choice = int(customInput.inputFormatted())

                if choice == 0:
                    print("Going back.")
                    break

                elif choice == 1:
                    pass

                elif choice == 2:
                    pass

                else:
                    print("Invalid input. Please try again.")
            
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
            pass #TBC

        else:
            print("Invalid input. Please try again.")
        
        print()
