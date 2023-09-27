from django.contrib import admin
from client.models import Client, Account, Purchase


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'cpf', 'email', 'birthday']
    list_editable = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


class AccountAdmin(admin.ModelAdmin):
    list_display = ['client', 'opened', 'total']
    ordering = ['client', 'total']
    list_editable = ['opened']
    search_fields = ['client']
    list_filter = ['opened']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['account', 'item', 'amount', 'total']
    list_filter = ['account']


admin.site.register(Client, ClientAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Purchase, PurchaseAdmin)
