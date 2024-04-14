import customInput
import dbConnection
import member

def setAvailability(connection, trainer):
    print("The following prompts are for setting your availability for the week. Please enter the days of the week and the times you are available.")
    print("Also note that each time slot is 1 hour long.")
    datetimes = customInput.inputDateTime()

    for day in datetimes:
        for time in datetimes[day]:
            for i in range(time[0], time[1]):
                query = f"INSERT INTO Availability (trainer_id, day_of_week, start_hour) VALUES ('{trainer['trainer_id']}', '{day}', '{i}')"
                dbConnection.executeQuery(connection, query)
    
    print("Availability set.")

def trainerSession(connection, trainer):
    while True:
        print("What would you like to do?")
        print("1. Set availability")
        print("2. View member profile")
        print("0. Log out")

        choice = int(customInput.inputFormatted())

        if choice == 0:
            print("Logging out.")
            break

        elif choice == 1:
            setAvailability(connection, trainer)

        elif choice == 2:
            print("Enter member name:")
            name = customInput.inputFormatted().split()

            query = f"SELECT * FROM Members NATURAL JOIN People WHERE first_name = '{name[0]}' AND last_name = '{name[1]}'"
            result = dbConnection.executeSelectQuery(connection, query, False)
            if result:
                member.viewProfile(connection, result)
            else:
                print("Member not found.")
        
        else:
            print("Invalid input. Please try again.")
        
        print()
