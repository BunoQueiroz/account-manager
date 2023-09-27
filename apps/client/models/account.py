from django.db import models
from .client import Client


class Account(models.Model):

    client = models.ForeignKey(Client, models.CASCADE)
    opened = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'account - {self.client.first_name}'
