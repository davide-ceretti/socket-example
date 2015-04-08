import os

import pika

from banter_wsgi import View, App, Response

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()


class Index(View):
    def get(self):
        return Response(
            open('static/index.html').read(),
            content_type="text/html"
        )

    def websocket(self):
        for method, properties, body in channel.consume("completes"):
            yield str(body)

routes = [
    ('/', 'index', Index),
]

app = App(routes)


if __name__ == "__main__":
    app.run(('', int(os.getenv('PORT', 8000))))
