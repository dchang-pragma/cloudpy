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
 
    db_config = read_db_config(filename='config.ini', section='mysql')
 
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
 
 
def query_with_fetchone():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
 
        row = cursor.fetchone()
 
        while row is not None:
            print(row)
            row = cursor.fetchone()
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
# if __name__ == '__main__':
#     query_with_fetchone()

 
 
def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        print(rows) # return list of tuples
        # print(rows[6][2])
 
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def do_nothing():
    pass
    
def query_with_fetchmany():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
 
        cursor.execute("SELECT * FROM books")
 
        for row in iter_row(cursor, 10):
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close() 
 
if __name__ == '__main__':
    query_with_fetchall()

 
# if __name__ == '__main__':
#     connect()