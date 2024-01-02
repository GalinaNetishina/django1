from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(decimal_places=1, max_digits=9)
    image = models.ImageField(upload_to='images')
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.slug} {self.name} {self.price} {self.lte_exists}"

