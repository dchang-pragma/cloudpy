from flask import Flask
from flask_restful import Resource, Api, reqparse
#from flask.ext.mysql import MySQL
from flaskext.mysql import MySQL
from py_config import read_db_config

app = Flask(__name__)
api = Api(app)

# class CreateUser(Resource):
#     def post(self):
#         return {'status': 'success'}

class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser() # Now create a parser from the reqparse libray.
            parser.add_argument('name', type=str, help='Name to create user')
            parser.add_argument('email', type=str, help='Email address to create user') #Using the parser, add the expected arguments.
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _name = args['name']
            _email = args['email']
            _password = args['password']
            if _name and _email and _password:
            	db_config = read_db_config()
            	mysql.init_app(app)
            	conn = mysql.connect()
            	cursor = conn.cursor()
            	cursor.callproc('sp_CreateUser',(_userEmail,_userPassword))
            	data = cursor.fetchall()
            	if len(data) is 0:
            		conn.commit()
            		return {'StatusCode':'200','Message': 'User creation success'}
            	else:
            		return {'StatusCode':'1000','Message': str(data[0])}

            return {'Name': args['name'], 'Email': args['email'], 'Password': args['password']}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/CreateUser')

if __name__ == '__main__':
    app.run(debug=True)