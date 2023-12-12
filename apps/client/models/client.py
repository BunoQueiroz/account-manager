from django.db import models
from uuid import uuid4


class Client(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4, auto_created=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=70, blank=True)
    cpf = models.CharField(max_length=14, blank=True)
    email = models.EmailField(blank=True)
    birthday = models.DateField()
    register_date = models.DateField(auto_now=True, editable=False)

    def __str__(self) -> str:
        if self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.first_name
    