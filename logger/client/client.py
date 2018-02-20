import sys

import pika

mq_connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
mq_channel = mq_connection.channel()

for line in sys.stdin:
    mq_channel.basic_publish('', 'logger', line.rstrip('\n'))

mq_channel.close()
mq_connection.close()
