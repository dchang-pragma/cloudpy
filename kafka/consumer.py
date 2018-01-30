import sys
import os

from confluent_kafka import Consumer, KafkaException, KafkaError
# brew install librdkafka; pip3 install confuent-kafka

if __name__ == '__main__':
    #topics = ["%s.test" % e89wzh2n-]
    #topics = ["%s.default" % os.environ['CLOUDKARAFKA_TOPIC_PREFIX']]
    #topics = ['e89wzh2n-default']

    # Consumer configuration
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    # conf = {
    #     'bootstrap.servers': 'velomobile-02.srvs.cloudkafka.com:9094,velomobile-01.srvs.cloudkafka.com:9094,velomobile-03.srvs.cloudkafka.com:9094',
    #     'group.id': "cloudkarafka-example",
    #     'session.timeout.ms': 6000,
    #     'default.topic.config': {'auto.offset.reset': 'smallest'},
    #     'security.protocol': 'SASL_SSL',
    #     'sasl.mechanisms': 'SCRAM-SHA-256',
    #     'sasl.username': 'e89wzh2n',
    #     'sasl.password': '_NxaDqtwQT6CKxQG2Q6HMKb9pwBG5aDj'
    # }


    conf = {
        'bootstrap.servers': 'velomobile-02.srvs.cloudkafka.com:9094,velomobile-01.srvs.cloudkafka.com:9094,velomobile-03.srvs.cloudkafka.com:9094',
        'group.id': "cloudkarafka-example",
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'smallest'},
        'security.protocol': 'ssl',
        #'sasl.mechanisms': 'SCRAM-SHA-256',
        # 'ssl.key.location': '~/.ssh/cloud_kafka/private_key3.pem',
        # 'ssl.ca.location': '~/.ssh/cloud_kafka/ca_cert3.pem',
        # 'ssl.certificate.location': '~/.ssh/cloud_kafka/signed_cert3.pem'
        'ssl.key.location': 'private_key3.key',
        'ssl.ca.location': 'ca_cert3.pem',
        'ssl.certificate.location': 'signed_cert3.cert'

    }

    c = Consumer(**conf)
    c.subscribe(['e89wzh2n-default'])
running = True
while running:
    msg = c.poll()
    if not msg.error():
        print('Received message: %s' % msg.value().decode('utf-8'))
    elif msg.error().code() != KafkaError._PARTITION_EOF:
        print(msg.error())
        running = False
c.close()