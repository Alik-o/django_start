from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(null=True, blank=True, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(null=True, blank=True, verbose_name='описание')
    image = models.ImageField(upload_to='images/', verbose_name='изображение', null=True, blank=True, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product', verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    publication_status = models.BooleanField(default=False, verbose_name='статус публикации')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', related_name='product')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        permissions = (
            ('can_publish_product', 'can publish product'),
        )
