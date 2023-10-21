from django.core.management.base import BaseCommand
from things.models import Thing

class Command(BaseCommand):
    help = 'Deletes seeded data'

    def handle(self, *args, **options):
        # Delete all records created by the seeder
        Thing.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully unseeded data.'))
