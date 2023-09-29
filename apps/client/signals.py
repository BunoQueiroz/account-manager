from client.models import Client, Account
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Client)
def create_account(sender, instance, created, *args, **kwargs):
    if created:
        Account.objects.create(client=instance)
