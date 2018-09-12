FROM gliderlabs/alpine:latest

MAINTAINER Wolfgang Paul Schmetterling <w.s@ahoj.net>

LABEL Description="Docker Advanced Course - Understanding Docker Images"

ADD . /pythonapp

WORKDIR /pythonapp

RUN apk-install python python-dev py-pip && pip install -r requirements.txt

CMD ["python", "app.py"]