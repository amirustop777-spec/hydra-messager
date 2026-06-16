from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):

    # username, password и дата регистрации уже есть в AbstractUser. Это лучше, чем писать с нуля

    about_me = models.TextField(max_length=100, blank=True, verbose_name='обо мне')
    friends = models.ManyToManyField('self', symmetrical=True, blank=True, verbose_name='друзья')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
