# Producer.py

from kafka import KafkaProducer
from kafka.errors import KafkaError
import os, ssl

# First get all info from the env
ca = os.environ.get('CLOUDKARAFKA_CA')
cert = os.environ.get('CLOUDKARAFKA_CERT')
key = os.environ.get('CLOUDKARAFKA_PRIVATE_KEY')
print(ca)
with open("/tmp/ca.pem", "w") as f:
    f.write(ca)
with open("/tmp/cert.pem", "w") as f:
    f.write(cert)
with open("/tmp/key.pem", "w") as f:
    f.write(key)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)

ssl_context.verify_mode = ssl.CERT_REQUIRED
ssl_context.check_hostname = True
ssl_context.load_verify_locations('/tmp/ca.pem')
ssl_context.load_cert_chain('/tmp/cert.pem', '/tmp/key.pem')

# Load the rest of the env variables
brokers = os.environ.get('CLOUDKARAFKA_BROKERS').split(',')
topic_prefix = os.environ.get('CLOUDKARAFKA_TOPIC_PREFIX')


producer = KafkaProducer(bootstrap_servers=brokers,
                         security_protocol='SSL',
                         ssl_context=ssl_context)

# Asynchronous by default
future = producer.send(topic_prefix + 'default', b'raw_bytes')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)