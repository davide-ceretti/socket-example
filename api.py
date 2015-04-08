import os
import sys

import pika

from banter_wsgi import View, App, Response

try:
    PORT = sys.argv[1]
except IndexError:
    PORT = 8000


class Index(View):
    def get(self):
        return Response(
            open('static/index.html').read().replace("{{PORT}}", str(PORT)),
            content_type="text/html"
        )

    def websocket(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost')
        )

        channel = connection.channel()
        result = channel.queue_declare(exclusive=True)
        queue = result.method.queue
        channel.queue_bind(
            exchange='completes', queue=queue, routing_key='foo'
        )
        for method, properties, body in channel.consume(queue):
            yield str(body)

routes = [
    ('/', 'index', Index),
]

app = App(routes)


if __name__ == "__main__":
    print "Starting appication on port {}".format(PORT)
    app.run(('', int(os.getenv('PORT', PORT))))
