import pika
import time
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()
channel.exchange_declare(exchange='completes')

i = 0
while 1:
    time.sleep(random.random() * 2)
    channel.basic_publish(
        exchange='completes',
        routing_key='foo',
        body=str(i)
    )
    i += 1
    print "Adding message {}".format(i)

connection.close()
