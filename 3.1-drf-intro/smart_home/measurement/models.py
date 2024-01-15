from django.utils.timezone import now

from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=150, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    created_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to=f'photos/{now().date()}', null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.created_at} - {self.temperature}'
