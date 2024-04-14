import customInput
import dbConnection
import member
import trainer
import admin

def memberRegistration(connection):
    print("Personal Information:")
    print("Enter your first name:")
    firstName = customInput.inputFormatted()
    print("Enter your last name:")
    lastName = customInput.inputFormatted()
    print("Enter your email:")
    email = customInput.inputFormatted()
    print("Enter your phone number:")
    phone = customInput.inputFormatted()
    print("Enter your address:")
    address = customInput.inputFormatted()
    print("Enter your age:")
    age = int(customInput.inputFormatted())
    print("Enter your gender:")
    gender = customInput.inputFormatted()

    print("Health Information:")
    print("Enter your current weight (in lbs):")
    initWeight = int(customInput.inputFormatted())
    print("Enter the weight you would like to achieve (in lbs):")
    targetWeight = int(customInput.inputFormatted())
    print("Enter your height (in inches):")
    height = int(customInput.inputFormatted())
    print("Enter your body fat percentage:")
    bodyFat = float(customInput.inputFormatted())
    print("Enter your fitness goal:")
    goal = customInput.inputFormatted()
    print("Enter the time in weeks you would like to achieve your goal:")
    timeWeeks = int(customInput.inputFormatted())
    print("Enter your balance($):")
    balance = float(customInput.inputFormatted())

    query = f"INSERT INTO People (first_name, last_name, phone_number, email, age, gender, address) VALUES ('{firstName}', '{lastName}', '{phone}', '{email}', '{age}', '{gender}', '{address}')"
    dbConnection.executeQuery(connection, query)

    personID = dbConnection.executeSelectQuery(connection, f"SELECT person_id FROM People WHERE email = '{email}'", False)["person_id"]

    query = f"INSERT INTO Members (person_id, init_weight, final_weight, height, body_fat, goal, time_weeks, balance) VALUES ('{personID}', '{initWeight}', '{targetWeight}', '{height}', '{bodyFat}', '{goal}', '{timeWeeks}', '{balance}')"
    dbConnection.executeQuery(connection, query)

    print("Sign up successful. Please log in.")

def main():
    connection = dbConnection.createConnection("healthclub", "postgres", "password", "127.0.0.1", "5432")

    while True:
        print("Welcome to the Health and Fitness Club!")
        print("Who are you logging in as?")
        print("1. Member")
        print("2. Trainer")
        print("3. Admin")
        print("0. Exit")
        role = int(customInput.inputFormatted())

        if role == 0:
            print("End of session.")
            break

        elif role == 1:
            print("1. Log in")
            print("2. Sign up")
            print("0. Cancel")

            choice = int(customInput.inputFormatted())

            if choice == 0:
                print("Cancelling.")
                continue

            if choice == 1:
                print("Enter your email:")
                email = customInput.inputFormatted()

                query = f"SELECT * FROM Members NATURAL JOIN People WHERE email = '{email}'"
                result = dbConnection.executeSelectQuery(connection, query, False)
                if result:
                    print("Logged in as Member.")
                    member.memberSession(connection, result)
                else:
                    print("Member not found.")
            
            elif choice == 2:
                memberRegistration(connection)
        
        elif role == 2:
            print("Enter your email:")
            email = customInput.inputFormatted()

            query = f"SELECT * FROM Trainers NATURAL JOIN People WHERE email = '{email}'"
            result = dbConnection.executeSelectQuery(connection, query, False)
            if result:
                print("Logged in as Trainer.")
                trainer.trainerSession(connection, result)
            else:
                print("Trainer not found.")
            
        elif role == 3:
            print("Logged in as Admin.")
            admin.adminSession(connection)
        
        else:
            print("Invalid input. Please try again.")
        
        print("End of session.\n")


if __name__ == "__main__":
    main()