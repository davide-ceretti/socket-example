socket-example
--------------

Requirements:
    Docker 1.5
    pika==0.9.8

* ```./run_rabbitmq.sh``` Run a rabbitmq container

* ```python add_messages.py``` Add some messages to the rabbitmq container on the queue "completes" every half second

* ```./build_api.sh; ./run_api.sh``` Build and run a container for a flask app fetching data from rabbitmq and publishing it via web sockets. See http://localhost:8001/ on your host.

Note: all commands run in interactive mode (no background daemon)
