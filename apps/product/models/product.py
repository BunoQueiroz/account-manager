from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=70)
    price = models.FloatField()
    criation_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    description = models.CharField(max_length=200, blank=True)
    brand = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.name
