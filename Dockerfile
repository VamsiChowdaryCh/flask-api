FROM alpine:latest

RUN apk add --update python3 py3-pip

COPY . .

RUN pip3 install -r requirements.txt

RUN chmod 0744 api.py

CMD ["usr/bin/python3", "api.py"]
