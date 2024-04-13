import psycopg2
from psycopg2 import OperationalError
import psycopg2.extras

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
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(query)
        connection.commit()
        # print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def executeSelectQuery(connection, query, getAll=True):
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(query)
        connection.commit()
        # print("Query executed successfully")

        if(getAll):
            result = cursor.fetchall()
            return result
    
        result = cursor.fetchone()
        return result

    except OperationalError as e:
        print(f"The error '{e}' occurred")