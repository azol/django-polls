#!/bin/sh

python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput

if [[ -n "${DJANGO_SUPERUSER_USERNAME}" ]] && [[ -n "${DJANGO_SUPERUSER_EMAIL}" ]]  && [[ -n "${DJANGO_SUPERUSER_PASSWORD}" ]]
then
  python3 manage.py ensuresuperuser
fi

exec "$@"
