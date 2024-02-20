FROM python:3

ENV PYTHONBUFFERD 1

ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /e-transport

WORKDIR /e-transport/

COPY . /e-transport

RUN python -m venv  /e-transport-env

ENV PATH="/e-transport-env/bin/:$PATH"

COPY entrypoint.sh /e-transport/entrypoint.sh

RUN python -m pip install --upgrade pip

COPY requirements.txt e-transport/

RUN pip install -r requirements.txt

