import logging
from time import sleep

import pika
import mongoengine

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

mongoengine.connect('docker', host='db')

class Message(mongoengine.Document):
    body = mongoengine.StringField(required=True)

mq_parameters = pika.ConnectionParameters(
    'rabbitmq', connection_attempts=5, retry_delay=4.2)
mq_connection = pika.BlockingConnection(mq_parameters)
mq_channel = mq_connection.channel()

mq_channel.queue_declare('ilovepromprog')
for _, _, body in mq_channel.consume('ilovepromprog'):
    logging.info('Received message: %s', body)
    Message(body=body).save()
