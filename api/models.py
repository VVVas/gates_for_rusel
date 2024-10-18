from django.db import models


class UserOS(models.Model):
    login = models.CharField(
        max_length=200,
        verbose_name='Имя пользователя в операционной системе',
        unique=True
    )

    add_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата обнаружения'
    )

    @property
    def num_pass(self) -> str:
        return self.login + str(self.add_date.timestamp())

    num_pass.fget.short_description = 'Номер пропуска'

    is_working = models.BooleanField(
        default=False,
        verbose_name='Пользователь работает'
    )

    class Meta:
        ordering = ('login',)
        verbose_name = 'Пользователь ОС'
        verbose_name_plural = 'Пользователи ОС'

    def __str__(self) -> str:
        return self.login


class Gate(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='Название КПП',
        unique=True
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'КПП'
        verbose_name_plural = 'КПП'

    def __str__(self) -> str:
        return self.title
