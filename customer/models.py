from django.db import models

# Create your models here.


class Customer(models.Model):
    userType = models.IntegerField(default=1)
    password = models.CharField(max_length=30)
    userName = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    phone = models.IntegerField(null=True)
    birthday = models.DateField(null=True)
    profile = models.ImageField(upload_to='/srv/cokassis/Client/image')


class HistoryKeyword(models.Model):
    keyword = models.CharField(max_length=30)
    searchCount = models.IntegerField()
    customer = models.ManyToManyField('Customer')


class Order(models.Model):
    customer = models.ForeignKey('Customer', blank=False)
    date = models.DateField(null=True)


class Dish(models.Model):
    discount = models.FloatField(default=1.0)
    estPrice = models.FloatField()
    Like = models.IntegerField(default=5)
    name = models.CharField(max_length=30)
    order = models.ManyToManyField('Order')
    customer = models.ForeignKey('Customer', blank=True)


class DishPhoto(models.Model):
    photo = models.ImageField(upload_to='/srv/cokassis/image')
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)


class SupMaterial(models.Model):
    breed = models.CharField(max_length=30)
    qtityInterval = models.CharField(max_length=30)
    dish = models.ManyToManyField('Dish', through='DishMat')


class DishMat(models.Model):
    Qtity = models.IntegerField()
    Unit = models.CharField(max_length=30)