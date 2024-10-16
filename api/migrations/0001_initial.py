# Generated by Django 5.1.2 on 2024-10-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='Название КПП')),
            ],
            options={
                'verbose_name': 'КПП',
                'verbose_name_plural': 'КПП',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='UserOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200, unique=True, verbose_name='Имя пользователя в операционной системе')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата обнаружения')),
                ('is_working', models.BooleanField(default=False, verbose_name='Пользователь работает')),
            ],
            options={
                'verbose_name': 'Пользователь ОС',
                'verbose_name_plural': 'Пользователи ОС',
                'ordering': ('login',),
            },
        ),
    ]
