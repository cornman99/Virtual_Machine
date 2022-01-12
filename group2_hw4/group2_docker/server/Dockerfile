FROM ubuntu

ADD httpserver.py /
RUN apt-get update
RUN apt-get install -y  python3
CMD python3 -m  httpserver.py


