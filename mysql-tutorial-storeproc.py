from mysql.connector import MySQLConnection, Error
from py_config import read_db_config
 
def call_find_all_sp():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
 
        cursor.callproc('find_all')
 
        # print out the result
        for result in cursor.stored_results():
            print(result.fetchall())
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
def call_find_by_isbn():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
 
        args = ['1236400967773', 0]
        result_args = cursor.callproc('find_by_isbn', args)
 
        print(result_args[1])
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
if __name__ == '__main__':
    call_find_by_isbn()