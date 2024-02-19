FROM python:3

ENV PYTHONBUFFERD 1

ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /e-transport

WORKDIR e-transport/

RUN pip install --upgrade pip


COPY . /e-transport

RUN pip install -r requirements.txt

COPY . e-transport/

