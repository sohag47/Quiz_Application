'''
from os import system, name
from time import sleep
# define our clear function


def screen_clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# print out some text
print('Hi !! I am Python\n'*10)
sleep(2)
# now call function we defined above
screen_clear()
'''
import psycopg2
from psycopg2 import Error
try:
    connection = psycopg2.connect(user="postgres",
                                  password="zxcv147bnm",
                                  host='127.0.0.1',
                                  port='5432',
                                  database="QuizApp"
                                  )
    cursor = connection.cursor()

    create_table_query = '''
    CREATE TABLE userinfo (
        ID INT PRIMARY KEY    NOT NULL,
        EMAIL TEXT NOT NULL,
        PASSWORD TEXT NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQ")


except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
