#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install django==4.0.6 whitenoise django-environ pillow requests django-tinymce mysqlclient gunicorn

python manage.py collectstatic --no-input

python manage.py migrate


