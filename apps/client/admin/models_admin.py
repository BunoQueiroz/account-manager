from django.contrib import admin
from django.http.response import HttpResponse
from client.admin.utils import reopen_account, update
from client.forms import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'cpf', 'email', 'birthday']
    list_editable = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    actions = [reopen_account]
    form = ClientForm

    def response_add(self, request, obj, post_url_continue: str | None = ...):
        if self.form.errors:
            HttpResponse.status_code = 400
        return super().response_add(request, obj, post_url_continue)


class AccountAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'opened', 'total', 'opening_date']
    @admin.display(ordering='client__first_name', description='client')
    def client_name(self, obj):
        return obj.client.first_name
    
    list_editable = ['opened']
    search_fields = ['client__first_name']
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
    