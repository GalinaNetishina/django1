from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(decimal_places=1)
    image = models.URLField
    release_date = models.DateField
    lte_exists = models.BooleanField
    slug = models.SlugField


