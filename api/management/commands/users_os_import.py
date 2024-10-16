import pwd

from django.core.management import BaseCommand

from ...models import UserOS


class Command(BaseCommand):
    help = 'Загрузка данных о пользователях ОС в БД'

    def handle(self, *args, **options):
        users_os = pwd.getpwall()
        for user in users_os:
            UserOS.objects.get_or_create(login=user.pw_name)
