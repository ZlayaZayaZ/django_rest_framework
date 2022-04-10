from django.db import models
from django.forms import ImageField


class Sensor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя датчика')
    description = models.CharField(max_length=50, verbose_name='Описание расположения')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return f'{self.id_sensor} - {self.created_at}'
