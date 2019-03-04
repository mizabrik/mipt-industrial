import logging
import random
import sys
import time

import pika

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

mq_parameters = pika.ConnectionParameters(
    'rabbitmq', connection_attempts=5, retry_delay=4.2)
mq_connection = pika.BlockingConnection(mq_parameters)
mq_channel = mq_connection.channel()

while True:
    sleep_time = random.randint(5, 20)
    logging.info('Sleeping for %d', sleep_time)
    time.sleep(sleep_time)

    body = str(random.randrange(100))
    mq_channel.basic_publish('', 'ilovepromprog', body)
    logging.info('Sent message: %s', body)

mq_channel.close()
mq_connection.close()
