from django.db import models


class Client(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=70, blank=True)
    cpf = models.CharField(max_length=14, blank=True)
    email = models.EmailField(blank=True)
    birthday = models.DateField()
