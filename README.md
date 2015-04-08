socket-example
--------------

Requirements:
    Docker 1.5

* ```./run_rabbitmq.sh``` Run a rabbitmq container

* ```python add_messages.py``` Add some messages to the rabbitmq container on the queue "completes" every half second

* ```python api.py <port>``` Run the api
