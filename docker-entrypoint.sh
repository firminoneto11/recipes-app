#!/bin/bash

set -e

echo "Applying migrations"
python3 manage.py migrate

echo "Running server at port 8000"
gunicorn --bind 0.0.0.0:8000 config.wsgi
