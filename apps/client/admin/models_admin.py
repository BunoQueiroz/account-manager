from django.contrib import admin
from django.http.response import HttpResponse
from client.admin.utils import reopen_account, update
from client.forms import ClientForm, PaymentForm


class ClientAdmin(admin.ModelAdmin):

    def id_client(self):
        return str(self.id)[0:8]
    
    list_display = [id_client, 'first_name', 'email', 'birthday']
    search_fields = ['first_name']
    actions = [reopen_account]
    list_per_page = 25
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
    list_per_page = 25


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['account', 'item', 'amount', 'total', 'moment']
    list_filter = ['account']
    actions = [update]
    list_per_page = 30


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['account', 'value', 'payer', 'moment', 'received']
    list_filter = ['account']
    search_fields = ['account', 'payer']
    list_per_page = 30
    form = PaymentForm

    def response_add(self, request, obj, post_url_continue: str | None = ...):
        if self.form.errors:
            HttpResponse.status_code = 400
        return super().response_add(request, obj, post_url_continue)


class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name', 'is_superuser']
    list_filter = ['is_superuser']
    search_fields = ['first_name', 'username']
    ordering = ['first_name']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class Manager(admin.AdminSite):
    site_header = 'Administration'
    