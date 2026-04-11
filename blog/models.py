from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='содержимое')
    preview = models.ImageField(upload_to='images/', verbose_name='превью', null=True, blank=True)
    publication_attribute = models.BooleanField(default=True, verbose_name='опубликовано')
    count_views = models.IntegerField(default=0, editable=False, verbose_name='просмотры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ['-created_at', '-count_views',]
