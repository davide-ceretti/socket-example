import pika
import time
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()
channel.queue_declare(queue='completes')

i = 0
while 1:
    time.sleep(random.random() * 2)
    channel.basic_publish(
        exchange='',
        routing_key='completes',
        body=str(i)
    )
    i += 1
    print "Adding message {}".format(i)

connection.close()
