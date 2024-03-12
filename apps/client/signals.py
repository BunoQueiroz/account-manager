from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User, Group, Permission
from client.models import (
    Client,
    Account,
    Payment,
    Purchase
)


@receiver(post_save, sender=Client)
def create_account(sender, instance, created, *args, **kwargs):
    if created:
        Account.objects.create(client=instance)


@receiver(post_delete, sender=Payment)
def recalculate_bill_total_after_deleting_payment(sender, instance: Payment, *args, **kwargs):
    Account.objects.get(client=instance.account.client).save(force_update=True)


@receiver(post_delete, sender=Purchase)
def recalculate_bill_total_after_deleting_purchase(sender, instance: Purchase, *args, **kwargs):
    Account.objects.get(client=instance.account.client).save(force_update=True)


@receiver(post_save, sender=User)
def set_permission_of_new_users(sender, instance: User, created, *args, **kwargs):
    
    def create_common_permissions():
        permissions_for_common_users = [
            'view_account',
            'view_client',
            'view_payment',
            'view_purchase',
            'view_category',
            'view_product',
            'add_client',
            'add_payment',
            'add_purchase',
            'add_category',
            'add_product',
            'change_client',
            'change_payment',
            'change_purchase',
            'change_category',
            'change_product',
        ]
        Group.objects.create(name='common_permissions')
        group = Group.objects.get(name='common_permissions')
        permissions = Permission.objects.all()
        for permission in permissions:
            if permission.codename in permissions_for_common_users:
                group.permissions.add(permission)
    
    if created:
        instance.is_staff = True
        common_permissions = Group.objects.filter(name='common_permissions')
        if not common_permissions.exists():
            create_common_permissions()
        instance.groups.add(common_permissions.get())
