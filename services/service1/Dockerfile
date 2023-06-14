FROM python:3.11.4-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt-get update -y
RUN apt-get install -y iputils-ping

COPY . .