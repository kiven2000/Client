from django.db import models

# Create your models here.


class Customer(models.Model):
    user_type = models.IntegerField(default=1)
    password = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    phone = models.IntegerField(null=True)
    birthday = models.DateField(null=True)
    profile = models.ImageField(upload_to='~/cokassis/Client/image')


class HistoryKeyword(models.Model):
    keyword = models.CharField(max_length=30)
    search_count = models.IntegerField()
    dish_type = models.BooleanField(default=True)
    mat_type = models.BooleanField(default=True)
    customers = models.ManyToManyField('Customer')

    class Meta:
        ordering = ['-keyword', '-search_count']

class Order(models.Model):
    customer = models.ForeignKey('Customer', blank=False)
    date = models.DateField(null=True)


class MatQuantity(models.Model):
    quantity = models.FloatField()