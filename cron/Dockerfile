FROM python:3.7.1

RUN set -ex && mkdir /app
RUN pip3 install -U setuptools pip
RUN pip3 install pipenv

WORKDIR /app

COPY cron/Pipfile* /app/

RUN pipenv sync

ADD cron /app
COPY settings.json /app
