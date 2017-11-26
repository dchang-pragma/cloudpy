from flask.ext.mysql import MySQL
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'jay'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
app.config['MYSQL_DATABASE_DB'] = 'ItemListDb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
cursor.callproc('spCreateUser',(_userEmail,_userPassword))
data = cursor.fetchall()
if len(data) is 0:
   conn.commit()
   return {'StatusCode':'200','Message': 'User creation success'}
else:
   return {'StatusCode':'1000','Message': str(data[0])}