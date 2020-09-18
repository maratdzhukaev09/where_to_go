from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    short_description = models.TextField(verbose_name='Краткое описание', default='', blank=True)
    long_description = HTMLField(verbose_name='Полное описание', default='', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    image = models.ImageField(verbose_name='Фотография')
    place = models.ForeignKey(to='Place', verbose_name='Место', on_delete=models.CASCADE, related_name='images')
    number = models.IntegerField(verbose_name='Номер картинки', blank=True, default=0)

    def __str__(self):
        return f'{self.number} {self.place.title}' if self.number else (f'{self.place.title}' if self.place else f'No Place {self.id}')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['number']
