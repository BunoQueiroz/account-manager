from django.contrib import admin
from client.models import Client, Account, Purchase
from django.contrib.auth.models import User, Group

# Update Action

@admin.action(description='Purchase Update')
def update(modeladmin, request, queryset):
    for instance in queryset:
        instance.save(update_fields=['total'])

# Admin Classes

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
    list_display = ['account', 'item', 'amount', 'total', 'moment']
    list_filter = ['account']
    actions = [update]


class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name', 'email', 'is_superuser']
    list_filter = ['is_superuser']
    search_fields = ['first_name', 'last_name']
    ordering = ['first_name']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class Manager(admin.AdminSite):
    site_header = 'Administration'
    

admin.site = Manager()

# Admin Register

admin.site.register(Client, ClientAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
