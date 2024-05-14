FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements/prod.txt /code/
RUN pip install -r prod.txt
ADD . /code/