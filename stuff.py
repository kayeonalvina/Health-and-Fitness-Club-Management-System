import psycopg2
from psycopg2 import OperationalError

def createConnection(dbName, dbUser, dbPassword, dbHost, dbPort):
    connection = None
    try:
        connection = psycopg2.connect(
            database=dbName,
            user=dbUser,
            password=dbPassword,
            host=dbHost,
            port=dbPort,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def executeQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")

        if(query.find("SELECT") != -1):
            result = cursor.fetchall()
            return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def main():
    connection = createConnection("healthclub", "postgres", "password", "127.0.0.1", "5432")

    print("Welcome to the Health and Fitness Club!")

    while True:
        print("Who are you logging in as?")
        print("1. Member")
        print("2. Trainer")
        print("3. Admin")
        print("0. Exit")
        role = int(input())

        if role == 0:
            print("End of session.")
            break

        elif role == 1:
            print("Enter your email:")
            email = input()

            query = f"SELECT * FROM Members NATURAL JOIN People WHERE email = '{email}'"
            result = executeQuery(connection, query)
            if result:
                print("Logged in as Member.")
                print(result)
            else:
                print("Member not found.")
        
        elif role == 2:
            print("Enter your email:")
            email = input()

            query = f"SELECT * FROM Trainers NATURAL JOIN People WHERE email = '{email}'"
            result = executeQuery(connection, query)
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