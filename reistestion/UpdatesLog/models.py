from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Лог'
