from flask import Flask
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL
from py_config import read_db_config

app = Flask(__name__)
api = Api(app)
mysql = MySQL()
mysql.init_app(app) # ----- has to be outside of class or function
# "A setup function was called after the first request was handled.  This usually indicates a bug in the application where a module was not imported and decorators or other functionality was called too late.\nTo fix this make sure to import all your view modules, database models and everything related at a central place before the application starts serving requests."

db_config = read_db_config(filename='config.ini', section='flask-mysql-cloudpy')
app.config['MYSQL_DATABASE_USER'] = db_config['user']
app.config['MYSQL_DATABASE_PASSWORD'] = db_config['password']
app.config['MYSQL_DATABASE_DB'] = db_config['database']
app.config['MYSQL_DATABASE_HOST'] = db_config['host']


# class CreateUser(Resource):
#     def post(self):
#         return {'status': 'success'}

class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser() # Now create a parser from the reqparse libray.
            parser.add_argument('name', type=str, help='Name to create user')
            parser.add_argument('email', type=str, help='Email address to create user') 
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()
            _name = args['name']
            _email = args['email']
            _password = args['password']
            if _name and _email and _password:
                #mysql.init_app(app)

                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.callproc('sp_CreateUser',(_name, _email, _password))
                data = cursor.fetchall()
                if len(data) is 0:
                    conn.commit()
                    return {'StatusCode':'200','Message': 'User creation success'}
                else:
                    return {'StatusCode':'1000','Message': str(data[0])}

            return {'Name': args['name'], 'Email': args['email'], 'Password': args['password']}

        except Exception as e:
            return {'error': str(e)}
        # finally:
        #     cursor.close()
        #     conn.close()

class AuthenticateUser(Resource):
    def post(self):
        try:
            # Parse the arguments

            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, help='Email address for Authentication')
            parser.add_argument('password', type=str, help='Password for Authentication')
            args = parser.parse_args()

            _userEmail = args['email']
            _userPassword = args['password']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_AuthenticateUser',(_userEmail,))
            data = cursor.fetchall()

            
            if(len(data)>0):
                print (data)
                if(str(data[0][3])==_userPassword):
                    return {'status':200,'UserId':str(data[0][0])}
                else:
                    return {'status':100,'message':'Authentication failure'}

        except Exception as e:
            return {'error': str(e)}


class AddItem(Resource):
    def post(self):
        try: 
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('item_name', type=str)
            args = parser.parse_args()

            _email = args['email']
            _item_name = args['item_name']

            #print _userId;

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_AddItems',(_email,_item_name))
            data = cursor.fetchall()

            conn.commit()
            return {'StatusCode':'200','Message': 'Success'}

        except Exception as e:
            return {'error': str(e)}


class GetAllItems(Resource):
    def post(self):
        try: 
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            args = parser.parse_args()

            _email = args['email']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_GetAllItems',(_email,))
            data = cursor.fetchall()

            items_list=[];
            for item in data:
                i = {
                    'item_id':item[0],
                    'item_name':item[1]
                }
                items_list.append(i)

            return {'StatusCode':'200','Items':items_list}

        except Exception as e:
            return {'error': str(e)}


api.add_resource(CreateUser, '/CreateUser')
api.add_resource(AuthenticateUser, '/AuthenticateUser')
api.add_resource(AddItem, '/AddItem')
api.add_resource(GetAllItems, '/GetAllItems')

if __name__ == '__main__':
    app.run(debug=True, port=5002)