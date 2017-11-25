# import mysql.connector #pip3 install mysql-connector-python
# from mysql.connector import Error
from mysql.connector import MySQLConnection, Error
from py_config import read_db_config



#import mysql.connector

# def connect():
#     """ Connect to MySQL database """
#     try:
#         conn = mysql.connector.connect(host='localhost',
#                                        database='python_mysql',
#                                        user='bunmaster',
#                                        password='password')
#         if conn.is_connected():
#             print('Connected to MySQL database')
#     except Error as e:
#         print(e)
#     finally:
#         conn.close()
# if __name__ == '__main__':
#     connect()

def connect():
    """ Connect to MySQL database """
 
    db_config = read_db_config()
 
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')
 
    except Error as error:
        print(error)
 
    finally:
        conn.close()
        print('Connection closed.')
 
 
if __name__ == '__main__':
    connect()