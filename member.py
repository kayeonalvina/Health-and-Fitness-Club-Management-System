import customInput
import dbConnection

def editProfile(connection, member):
    print("What edit would you like to make?")
    print("1. Personal information")
    print("2. Health information")

    choice = int(customInput.inputFormatted())

    if choice == 1:
        print("What would you like to edit?")
        print("1. First name")
        print("2. Last name")
        print("3. Phone number")
        print("4. Email")
        print("5. Age")
        print("6. Address")

        edit = int(customInput.inputFormatted())

        if edit == 1:
            print("Enter new first name:")
            first_name = customInput.inputFormatted()
            query = f"UPDATE People SET first_name = '{first_name}' WHERE person_id = '{member['person_id']}'"
            dbConnection.executeQuery(connection, query)
        
        elif edit == 2:
            print("Enter new last name:")
            last_name = customInput.inputFormatted()
            query = f"UPDATE People SET last_name = '{last_name}' WHERE person_id = '{member['person_id']}'"
            dbConnection.executeQuery(connection, query)
        
        elif edit == 3:
            print("Enter new phone number:")
            phone_number = customInput.inputFormatted()
            query = f"UPDATE People SET phone_number = '{phone_number}' WHERE person_id = '{member['person_id']}'"
            dbConnection.executeQuery(connection, query)
        
        elif edit == 4:
            print("Enter new email:")
            email = customInput.inputFormatted()
            query = f"UPDATE People SET email = '{email}' WHERE person_id = '{member['person_id']}'"
            dbConnection.executeQuery(connection, query)
        
        elif edit == 5:
            print("Enter new age:")
            age = int(customInput.inputFormatted())
            query = f"UPDATE People SET age = {age} WHERE person_id = '{member['person_id']}'"
            dbConnection.executeQuery(connection, query)
        
        elif edit == 6:
            print("Enter new address:")
            address = customInput.inputFormatted()
            query = f"UPDATE People SET address = '{address}' WHERE person_id = '{member['person_id']}'"
            dbConnection.executeQuery(connection, query)
        
        else:
            print("Invalid input. Please try again.")
    
    elif choice == 2:
        print("What would you like to edit?")
        print("1. Initial weight")
        print("2. Target weight")
        print("3. Height")
        print("4. Body fat percentage")
        print("5. Fitness goal")
        print("6. Timeframe")
        #Balance is not changeable, we assume

        edit = int(customInput.inputFormatted())

        if edit == 1:
            print("Enter new initial weight:")
            initial_weight = float(customInput.inputFormatted())
            query = f"UPDATE Members SET init_weight = {initial_weight} WHERE member_id = '{member['member_id']}'"
            dbConnection.executeQuery(connection, query)

        elif edit == 2:
            print("Enter new target weight:")
            target_weight = float(customInput.inputFormatted())
            query = f"UPDATE Members SET final_weight = {target_weight} WHERE member_id = '{member['member_id']}'"
            dbConnection.executeQuery(connection, query)
        
        elif edit == 3:
            print("Enter new height:")
            height = float(customInput.inputFormatted())
            query = f"UPDATE Members SET height = {height} WHERE member_id = '{member['member_id']}'"
            dbConnection.executeQuery(connection, query)
        
        elif edit == 4:
            print("Enter new body fat percentage:")
            body_fat_percentage = float(customInput.inputFormatted())
            query = f"UPDATE Members SET body_fat = {body_fat_percentage} WHERE member_id = '{member['member_id']}'"
            dbConnection.executeQuery(connection, query)
        
        elif edit == 5:
            print("Enter new fitness goal:")
            fitness_goal = customInput.inputFormatted()
            query = f"UPDATE Members SET goal = '{fitness_goal}' WHERE member_id = '{member['member_id']}'"
            dbConnection.executeQuery(connection, query)
        
        elif edit == 6:
            print("Enter new timeframe:")
            timeframe = customInput.inputFormatted()
            query = f"UPDATE Members SET time_weeks = '{timeframe}' WHERE member_id = '{member['member_id']}'"
            dbConnection.executeQuery(connection, query)
        
        else:
            print("Invalid input. Please try again.")

def addEvent(connection, member, schedule):
    pass #TBC

def removeEvent(connection, member, schedule):
    while True:
        print("Enter the event ID you would like to remove(-1 to cancel):")
        eventID = int(customInput.inputFormatted())

        if(eventID == -1):
            print("Cancelling removal.")
            break

        elif eventID < 1 or eventID > len(schedule):
            print("Invalid event ID. Please try again.")
        
        else:
            print(f"Are you sure you want to remove event {eventID}? (y/n)")
            confirm = customInput.inputFormatted()

            if confirm == "y":
                query = f"DELETE FROM MemberEvents WHERE event_id = '{schedule[eventID - 1]['event_id']}'"
                dbConnection.executeQuery(connection, query)
                print("Event removed.")
                break


def memberSession(connection, member):
    print("What would you like to do?")

    while True:
        print("1. View and edit profile")
        print("2. View dashboard")
        print("3. Manage schedule")
        print("0. Log out")

        choice = int(customInput.inputFormatted())

        if choice == 0:
            print("Logging out.")
            break

        elif choice == 1:
            print("Your profile:")
            
            print("\nPersonal information:")
            print("Name:", member['first_name'], member['last_name'])
            print("Phone number:", member['phone_number'])
            print("Email:", member['email'])
            print("Age:", member['age'])
            print("Address:", member['address'])

            print("\nHealth information:")
            print("Initial weight:", member['init_weight'])
            print("Target weight:", member['final_weight'])
            print("Height:", member['height'])
            print("Body fat percentage:", member['body_fat'])
            print("Fitness goal:", member['goal'])
            print("Timeframe:", member['time_weeks'])
            print("Balance:", member['balance'])

            print("\nWould you like to edit your profile? (y/n)")

            edit = customInput.inputFormatted()

            if edit == "y":
                editProfile(connection, member)
                print("Updating process complete.")
            
        elif choice == 2:
            print("Your dashboard:")

            print("\nExercise Routine:\n", dbConnection.executeSelectQuery(connection, f"SELECT description FROM ExerciseRoutines NATURAL JOIN Members WHERE member_id = '{member['routine_id']}'"))

            print("Fitness Achievements:\n", dbConnection.executeSelectQuery(connection, f"SELECT description, date_achieved FROM MemberAchievements NATURAL JOIN FitnessAchievements WHERE member_id = '{member['member_id']}'"), False)

            print("Health information:")
            print("Fitness goal:", member['goal'])
            print("Timeframe:", member['time_weeks'])

        elif choice == 3:
            print("Your schedule:")
            schedule = dbConnection.executeSelectQuery(connection, f"SELECT * FROM MemberEvents NATURAL JOIN Events WHERE member_id = '{member['member_id']}'")

            eventID = 1
            daysOfWeek = {
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
            }

            for event in schedule:
                trainerName = dbConnection.executeSelectQuery(connection, f"SELECT first_name, last_name FROM Trainers NATURAL JOIN People WHERE trainer_id = '{event['trainer_id']}'", False)
                trainerName = f"{trainerName['first_name']} {trainerName['last_name']}"
                print(f"ID: {eventID}: {daysOfWeek[event['day_of_week']]}, {event['start_hour']} - {event['end_hour']}: Room #{event['room']} with {trainerName}")
                eventID += 1
            
            print("\n Would you like to make any changes to your schedule? (y/n)")
            change = customInput.inputFormatted()

            if change == "y":
                print("What would you like to do?")
                print("1. Add event")
                print("2. Remove event")

                action = int(customInput.inputFormatted())

                if action == 1:
                    addEvent(connection, member, schedule)
                
                elif action == 2:
                    removeEvent(connection, member, schedule)
                
                else:
                    print("Invalid input. Please try again.")
        
        else:
            print("Invalid input. Please try again.")
    
        print()