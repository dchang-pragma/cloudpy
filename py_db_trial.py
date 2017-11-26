from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from py_config import read_db_config

def connect():
    """ Connect to MySQL database """
 
    app = Flask(__name__)
    mysql = MySQL()
    mysql.init_app(app)
    
    db_config = read_db_config(filename='config.ini', section='flask-mysql-pyweb')
    #print (db_config)
    #conn = mysql.connect(**db_config)
    app.config['MYSQL_DATABASE_USER'] = db_config['user']
    app.config['MYSQL_DATABASE_PASSWORD'] = db_config['password']
    app.config['MYSQL_DATABASE_DB'] = db_config['database']
    app.config['MYSQL_DATABASE_HOST'] = db_config['host']
    print (app.config)
 
    # try:
    #     print('Connecting to MySQL database...')
    #     #conn = mysql.connect(**db_config)
    #     conn = mysql.connect()
 
    #     if conn.is_connected():
    #         print('connection established.')
    #     else:
    #         print('connection failed.')
 
    # except Error as error:
    #     print(error)
 
    # finally:
    #     conn.close()
    #     print('Connection closed.')

if __name__ == '__main__':
    connect()