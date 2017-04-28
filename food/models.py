from django.db import models

# Create your models here.


class Dish(models.Model):
    estPrice = models.FloatField()
    name = models.CharField(max_length=30)
    discount = models.FloatField(default=1.0)
    like = models.IntegerField(default=5)


class DishMat(models.Model):
    Qtity = models.IntegerField()
    Unit = models.CharField(max_length=30)


class DishPhoto(models.Model):
    photo = models.ImageField(upload_to='/srv/cokassis/image')


class Material(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)


class WeightInterval(models.Model):
    interval = models.FloatField()
    note = models.CharField(max_length=30)