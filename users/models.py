from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=100, verbose_name="Имя пользователя", blank=True, null=True, unique=False)
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to="users/avatars", blank=True, null=True, verbose_name="Avatar")
    phone = models.CharField(max_length=13, blank=True, null=True, verbose_name='Номер телефона')
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name='Страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
