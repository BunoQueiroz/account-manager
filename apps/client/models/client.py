from django.db import models


class Client(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=70, blank=True)
    cpf = models.CharField(max_length=14, blank=True)
    email = models.EmailField(blank=True)
    birthday = models.DateField()

    def __str__(self) -> str:
        if self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.first_name
    