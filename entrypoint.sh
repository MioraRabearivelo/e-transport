#!/bin/bash

set -e

source /e-transport-env/bin/activate

python manage.py makemigrations

python manage.py migrate

if [$1 == 'gunicorn'];then
    exec gunicorn transit.wsgi:application -b  0.0.0.0:8000
else
    exec python manage.py runserver 0.0.0.0:8000
fi