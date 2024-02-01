from django.db import models
from client.models import Client
from product.models import Product
from django.contrib.auth.models import User
from uuid import uuid4


class Account(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4, auto_created=True)
    client = models.OneToOneField(Client, models.CASCADE)
    opening_date = models.DateField(auto_now=True, editable=False)
    opened = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=9, decimal_places=2, editable=False)

    def __str__(self) -> str:
        return f'Account - {self.client.first_name}'
    
    def total_account(self, force_update=None) -> float:
        if force_update is not None:
            payments = Payment.objects.filter(account=self)
            purchases = Purchase.objects.filter(account=self)
            if payments and purchases:
                sum_purchases = sum(purchase.total for purchase in purchases)
                sum_payments = sum(payment.value for payment in payments)
                return sum_purchases - sum_payments
            return sum(purchase.total for purchase in purchases)
        return 0
    
    def save(self, force_insert=False, using=False, force_update=None) -> None:
        self.total = self.total_account(force_update)
        return super().save(force_insert, using=using, force_update=force_update)


class Purchase(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4, auto_created=True)
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


class Payment(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4, auto_created=True)
    moment = models.DateTimeField(auto_created=True, editable=False, auto_now=True)
    value = models.FloatField()
    received = models.ForeignKey(User, models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    payer = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.payer} -> {self.moment.date()}'

    def save(self, force_insert=False , force_update=False) -> None:
        super().save(force_insert, force_update)
        return self.account.save(force_insert=False, using=False, force_update=True)
    