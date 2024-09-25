#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install pillow requests django-tinymce

python manage.py collectstatic --no-input

python manage.py migrate


