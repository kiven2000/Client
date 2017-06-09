from django.db import models

# Create your models here.


class Dish(models.Model):
    estPrice = models.FloatField()
    name = models.CharField(max_length=30)
    discount = models.FloatField(default=1.0)
    like = models.IntegerField(default=5)
    customer = models.ForeignKey('customer.Customer')


class DishMat(models.Model):
    quantity = models.IntegerField()
    material = models.ForeignKey('Material')
    unit = models.CharField(max_length=30)
    dish = models.ForeignKey('Dish')
    weightInterval = models.OneToOneField('WeightInterval')
    supplier = models.OneToOneField('supplier.Supplier')


class DishPhoto(models.Model):
    photo = models.ImageField(upload_to='~/cokassis/image')
    dish = models.ForeignKey('Dish')


class Material(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    alias = models.CharField(max_length=30, null=True)
    dish = models.ManyToManyField(
        'Dish',
        through='DishMat',
        through_fields=('material', 'dish'),
    )


class WeightInterval(models.Model):
    intervalMaxWeight = models.FloatField()
    intervalMinWeight = models.FloatField()
    intervalNote = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    material = models.ForeignKey('Material')
