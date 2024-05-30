#!/bin/sh

pip3 install --no-cache-dir -r requirements.txt
python3 manage.py collectstatic --noinput --clear
python3 manage.py migrate --noinput

if [[ -n "${DJANGO_SUPERUSER_USERNAME}" ]] && [[ -n "${DJANGO_SUPERUSER_EMAIL}" ]]  && [[ -n "${DJANGO_SUPERUSER_PASSWORD}" ]]
then
  python3 manage.py ensuresuperuser
fi
