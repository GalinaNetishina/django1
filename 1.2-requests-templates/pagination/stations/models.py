from django.db import models


class BusRoute(models.Model):
    number = models.CharField(max_length=5)


class AdmArea(models.Model):
    name = models.CharField(max_length=30)


class District(models.Model):
    name = models.CharField(max_length=30)


class BusStation(models.Model):
    global_id = models.IntegerField()
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    latitude = models.DecimalField(max_digits=11, decimal_places=8)
    adm_area = models.ForeignKey(AdmArea, on_delete=models.CASCADE, related_name='stations')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='stations')
    routes = models.ManyToManyField(BusRoute, related_name='stations')
    address = models.CharField(max_length=80)
    station_name = models.CharField(max_length=30)
    direction = models.CharField(max_length=10)
    pavilion = models.BooleanField()
    operating_org = models.CharField(max_length=30)
