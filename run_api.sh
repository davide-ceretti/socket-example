docker run -t -i --rm -p 8001:8001 -v `pwd`:/code/work --name web --link rabbit:rabbit socket-example
