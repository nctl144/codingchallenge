# pull official base image
FROM python:3.10.7-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y netcat

ENV FLASK_APP=app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /app

ENTRYPOINT ["flask", "run"]