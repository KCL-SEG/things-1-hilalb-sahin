from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from faker import Faker
from things.models import Thing

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--total', type=int, default=100)

    def handle(self, *args, **options):
        total = options['total']
        self.stdout.write(f'Seeding {total} things...')
        self.seed_things(total)
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {total} things.'))

    def seed_things(self, total):
        faker = Faker()
        for _ in range(total):
            name = self.generate_unique_name()
            description = faker.sentence()
            quantity = faker.random_int(min=1, max=100)
            thing = Thing(name=name, description=description, quantity=quantity)
            thing.save()

    def generate_unique_name(self):
        while True:
            name = get_random_string(10)
            if not Thing.objects.filter(name=name).exists():
                return name
