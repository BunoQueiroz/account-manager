from django.contrib import admin
from client.models import Account


@admin.action(description='Purchase Update')
def update(modeladmin, request, queryset):
    for instance in queryset:
        instance.save(update_fields=['total'])

@admin.action(description='Reopen Account')
def reopen_account(modeladmin, request, queryset):
    for instance in queryset:
        Account.objects.get_or_create(client=instance)
