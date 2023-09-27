from django.db import models
from client.models import Client
from product.models import Product


class Account(models.Model):

    client = models.OneToOneField(Client, models.CASCADE)
    opened = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=9, decimal_places=2, editable=False)

    def __str__(self) -> str:
        return f'account - {self.client.first_name}'
    
    def total_account(self) -> float:
        total = 0
        purchases = Purchase.objects.filter(account=self)
        total = sum(purchase.total for purchase in purchases)
        return total
    
    def save(self) -> None:
        self.total = self.total_account()
        return super().save()


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
        return super().save()
