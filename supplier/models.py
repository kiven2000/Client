from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=30)


class MatSellInfo(models.Model):
    unitPrice = models.FloatField()