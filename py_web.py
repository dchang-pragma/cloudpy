from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
#import pymysql # pymysql is another alternative
from werkzeug import generate_password_hash, check_password_hash
from py_config import read_db_config


app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
db_config = read_db_config(filename='config.ini', section='flask-mysql-pyweb')
#print (db_config)
#conn = mysql.connect(**db_config)
app.config['MYSQL_DATABASE_USER'] = db_config['user']
app.config['MYSQL_DATABASE_PASSWORD'] = db_config['password']
app.config['MYSQL_DATABASE_DB'] = db_config['database']
app.config['MYSQL_DATABASE_HOST'] = db_config['host']

mysql.init_app(app)
# conn = mysql.connect()
# cursor = conn.cursor()

@app.route("/")
def main():
	return render_template('index.html')
	
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

# @app.route('/signUp',methods=['POST'])
# def signUp():
#     # create user code will be here; read the posted values from the UI
#     _name = request.form['inputName']
#     _email = request.form['inputEmail']
#     _password = request.form['inputPassword']
#     if _name and _email and _password:
#         return json.dumps({'html':'<span>All fields good !!</span>'})
#     else:
#         return json.dumps({'html':'<span>Enter the required fields</span>'})

@app.route('/signUp',methods=['POST'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:

            # All Good, let's call MySQL

            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()



if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(port=5000)