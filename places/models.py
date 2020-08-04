from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    short_description = models.TextField(verbose_name='Краткое описание')
    long_description = models.TextField(verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    image = models.ImageField(verbose_name='Фотография')
    place = models.ForeignKey(to='Place', verbose_name='Место', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.place.title}'
