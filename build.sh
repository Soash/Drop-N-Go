#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt

pip install pillow requests django-tinymce psycopg2-binary


python manage.py collectstatic --no-input

python manage.py migrate


