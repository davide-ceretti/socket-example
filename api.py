import pika

from flask import Flask
from flask_sockets import Sockets

app = Flask(__name__)
app.debug = True
sockets = Sockets(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@sockets.route('/socket')
def echo_socket(ws):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('rabbit')
    )

    channel = connection.channel()
    channel.queue_declare(queue='completes')

    def callback(ch, method, properties, body):
        ws.send(body)

    channel.basic_consume(callback, queue='completes', no_ack=True)
    channel.start_consuming()
