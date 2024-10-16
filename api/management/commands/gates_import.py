import os
from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand

from ...models import Gate

DATA = os.path.join(settings.BASE_DIR, 'data', 'gates.csv')


class Command(BaseCommand):
    help = 'Загрузка данных о КПП из файла в БД'

    def handle(self, *args, **options):
        with open(DATA, mode='r', encoding='utf8') as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                Gate.objects.get_or_create(**row)
