from cassandra.cluster import Cluster
import cassandra; print(cassandra.__version__)'

cluster = Cluster(['127.0.0.1'])
#session = cluster.connect('mykeyspace')
#session.set_keyspace('mykeyspace')
session = cluster.connect()
#session.set_keyspace('users')
#rows = session.execute('SELECT name, age, email FROM users')
#cqlsh - CREATE KEYSPACE bun1 WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 2};
rows = session.execute('SELECT cluster_name, listen_address FROM system.local;')
for row in rows:
	print (row.cluster_name, row.listen_address)