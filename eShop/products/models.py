from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.URLField(max_length=2083, null=True)


class Offer(models.Model):
    code = models.CharField(max_length=100)
    description = models.TextField()
    value = models.DecimalField(max_digits=5, decimal_places=2)