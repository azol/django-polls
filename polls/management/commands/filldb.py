from django.core.management import BaseCommand, call_command
from django.utils import timezone
from faker import Faker

from polls.models import Choice
from polls.models import Question as Poll


class Command(BaseCommand):
    help = "Fills the database with Faker data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Removes ALL DATA from the database before filling",
        )

    def handle(self, *args, **options):
        if options["flush"]:
            call_command("flush", "--noinput")

        fake = Faker()
        Faker.seed(timezone.now().timestamp())
        choices = [
            list(set([fake.android_platform_token() for _ in range(10)])),
            list(set([fake.chrome() for _ in range(10)])),
            list(set([fake.firefox() for _ in range(10)])),
            list(set([fake.internet_explorer() for _ in range(10)])),
            list(set([fake.ios_platform_token() for _ in range(10)])),
            list(set([fake.linux_platform_token() for _ in range(10)])),
            list(set([fake.linux_processor() for _ in range(10)])),
            list(set([fake.mac_platform_token() for _ in range(10)])),
            list(set([fake.mac_processor() for _ in range(10)])),
            list(set([fake.opera() for _ in range(10)])),
            list(set([fake.safari() for _ in range(10)])),
            list(set([fake.user_agent() for _ in range(10)])),
            list(set([fake.windows_platform_token() for _ in range(10)])),
        ]

        for _ in range(5):
            poll = Poll.objects.create(
                question_text=fake.sentence(nb_words=10),
                pub_date=fake.date_time(tzinfo=fake.pytimezone()),
            )

            choices_for_poll = fake.random_sample(fake.random_element(choices))
            for choice in choices_for_poll:
                Choice.objects.create(
                    question=poll,
                    choice_text=choice,
                )

        self.stdout.write(self.style.SUCCESS("Successfully added polls"))
