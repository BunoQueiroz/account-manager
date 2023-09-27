from django.db import models
from client.models import Account
from product.models import Product


class Purchase(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField(default=1)
    moment = models.DateTimeField(auto_now=True, editable=False)
    total = models.FloatField(editable=False)

    def total_purchase(self) -> float:
        return (self.amount * self.item.price)
    
    def __str__(self) -> str:
        return f'{self.account.client.first_name} - {self.moment.date()}'

    def save(self) -> None:
        self.total = self.total_purchase()
        return super().save(self)
