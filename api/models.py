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


class Visit(models.Model):
    user = models.ForeignKey(
        UserOS,
        on_delete=models.CASCADE,
        related_name='visit',
        verbose_name='Пользователь ОС'
    )
    is_enter = models.BooleanField(
        default=None,
        verbose_name='Пользователь вошёл'
    )
    gate = models.ForeignKey(
        Gate,
        on_delete=models.CASCADE,
        related_name='visit',
        verbose_name='КПП'
    )
    num_pass = models.CharField(
        max_length=600,
        verbose_name='Номер пропуска'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата прохода'
    )

    class Meta:
        ordering = ('date',)
        verbose_name = 'Проход пользователя ОС'
        verbose_name_plural = 'Проходы пользователей ОС'

    def __str__(self) -> str:
        text_is_enter = 'вошёл' if self.is_enter else 'вышёл'
        return f'{self.user} {text_is_enter} в {self.date} с {self.num_pass}'
