import customInput
import dbConnection
import member

def main():
    connection = dbConnection.createConnection("healthclub", "postgres", "password", "127.0.0.1", "5432")

    print("Welcome to the Health and Fitness Club!")

    while True:
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
            print("Enter your email:")
            email = customInput.inputFormatted()

            query = f"SELECT * FROM Members NATURAL JOIN People WHERE email = '{email}'"
            result = dbConnection.executeSelectQuery(connection, query, False)
            if result:
                print("Logged in as Member.")
                member.memberSession(connection, result)
            else:
                print("Member not found.")
        
        elif role == 2:
            print("Enter your email:")
            email = customInput.inputFormatted()

            query = f"SELECT * FROM Trainers NATURAL JOIN People WHERE email = '{email}'"
            result = dbConnection.executeSelectQuery(connection, query, False)
            if result:
                print("Logged in as Trainer.")
                print(result)
            else:
                print("Trainer not found.")
            
        elif role == 3:
            print("Logged in as Admin.")
        
        else:
            print("Invalid input. Please try again.")
        
        print("End of session.\n")


if __name__ == "__main__":
    main()