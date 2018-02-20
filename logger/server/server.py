from time import sleep

import pika
import mongoengine

mongoengine.connect('logger', host='db')

class Message(mongoengine.Document):
    text = mongoengine.StringField(required=True)

mq_parameters = pika.ConnectionParameters('rabbitmq')
mq_connection = None
while mq_connection is None:
    try:
        mq_connection = pika.BlockingConnection(mq_parameters)
    except pika.exceptions.ConnectionClosed:
        sleep(4.2)
mq_channel = mq_connection.channel()

mq_channel.queue_declare("logger")
for _, _, body in mq_channel.consume('logger'):
    Message(text=body).save()
