from django.db import models
from client.models import Client
from product.models import Product


class Account(models.Model):

    client = models.OneToOneField(Client, models.CASCADE)
    opening_date = models.DateField(auto_now=True, editable=False)
    opened = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=9, decimal_places=2, editable=False)

    def __str__(self) -> str:
        return f'Account - {self.client.first_name}'
    
    def total_account(self, force_update=None) -> float:
        if force_update is not None:
            purchases = Purchase.objects.filter(account=self)
            return sum(purchase.total for purchase in purchases)
        return 0
    
    def save(self, force_insert=False, using=False, force_update=None) -> None:
        self.total = self.total_account(force_update)
        return super().save(force_insert, using=using, force_update=force_update)


class Purchase(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.FloatField(default=1)
    moment = models.DateTimeField(auto_now=True, editable=False)
    total = models.FloatField(editable=False)

    def total_purchase(self) -> float:
        return (self.amount * self.item.price)
    
    def __str__(self) -> str:
        return f'{self.account.client.first_name} - {self.moment.date()}'

    def save(self, force_insert=False, using=False, update_fields=False) -> None:
        self.total = self.total_purchase()
        if update_fields:
            super().save(update_fields=update_fields)
        else:
            super().save(force_insert=force_insert, using=using)
        return self.account.save(force_update=True)
