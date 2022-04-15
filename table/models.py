from django.db import models

class Table(models.Model):
    date = models.DateField(verbose_name='Дата')
    title = models.CharField(max_length=250, verbose_name='Название')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    distance = models.FloatField(verbose_name='Расстояние')

    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'

    def __str__(self):
        return self.title
