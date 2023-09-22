from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)


class Product(models.Model):

    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    criation_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)

