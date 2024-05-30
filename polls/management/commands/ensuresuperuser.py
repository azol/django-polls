"""
Management utility to create superusers.
"""

import os

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Used to create a superuser."

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if username is None or email is None or password is None:
            return

        if not User.objects.filter(username=username).exists():
            call_command("createsuperuser", "--noinput")
        else:
            try:
                user = User.objects.get(username=username, is_superuser=True)
                user.email = email
                user.set_password(password)
                user.save()
            except Exception:
                pass
