from django.db import models
from uuid import uuid4


class Category(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4, auto_created=True)
    name = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now=True, editable=False)
    update_date = models.DateField(auto_now=True, auto_created=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4, auto_created=True)
    name = models.CharField(max_length=70)
    price = models.FloatField()
    creation_date = models.DateField(auto_now=True, editable=False)
    update_date = models.DateField(auto_now=True, auto_created=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    description = models.CharField(max_length=200, blank=True)
    brand = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.name
