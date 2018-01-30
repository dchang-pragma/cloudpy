from kafka import KafkaConsumer
# consumer = KafkaConsumer('buntalk01')
consumer = KafkaConsumer('buntalk01',
                         #group_id='my-group',
                         bootstrap_servers=['localhost:9092'])
for msg in consumer:
  print (msg)