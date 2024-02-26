# django-polls

django-polls is a Django app to conduct web-based polls. For each
question, visitors can choose between a fixed number of answers.

Django Tutorial: https://docs.djangoproject.com/en/5.0/intro/tutorial01/

Online Demo: https://django-polls-one.vercel.app/polls/

## Install

```sh
pip install -r requirements.txt
python manage.py collectstatic
python manage.py migrate
python manage.py createsuperuser
```

## Start the development server

```sh
python manage.py runserver
```

## Quick start

- Start the development server and visit the admin at `/admin/` URL to create a poll.
- Visit the `/polls/` URL to participate in the poll.

##  Running in Gunicorn behind a proxy server

```sh
gunicorn mysite.wsgi
openssl req -x509 -nodes -newkey rsa:2048 -keyout nginx/domain.key -out nginx/domain.crt
nginx -c $PWD/nginx/nginx.conf
```
