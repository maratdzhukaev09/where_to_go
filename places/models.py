from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    short_description = models.TextField(verbose_name='Краткое описание', null=True, blank=True)
    long_description = models.TextField(verbose_name='Полное описание', null=True, blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    image = models.ImageField(verbose_name='Фотография')
    place = models.ForeignKey(to='Place', verbose_name='Место', on_delete=models.CASCADE, null=True, related_name='images')
    number = models.IntegerField(verbose_name='Номер картинки', null=True, blank=True, default=0)

    def __str__(self):
        return f'{self.number} {self.place.title}' if self.number else f'{self.place.title}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['number']
