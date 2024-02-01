from client.models import Client, Account, Payment, Purchase
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


@receiver(post_save, sender=Client)
def create_account(sender, instance, created, *args, **kwargs):
    if created:
        Account.objects.create(client=instance)


@receiver(post_delete, sender=Payment)
def recalculate_bill_total_after_deleting_payment(sender, instance, *args, **kwargs):
    Account.objects.get(client=instance.account.client).save(force_update=True)


@receiver(post_delete, sender=Purchase)
def recalculate_bill_total_after_deleting_purchase(sender, instance, *args, **kwargs):
    Account.objects.get(client=instance.account.client).save(force_update=True)
