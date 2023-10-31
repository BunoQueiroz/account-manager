from django.contrib import admin
from client.models import Client, Account, Purchase
from django.contrib.auth.models import User, Group
from client.admin.models_admin import ClientAdmin, AccountAdmin, PurchaseAdmin, UserAdmin, GroupAdmin, Manager


admin.site = Manager()

# Admin Register

admin.site.register(Client, ClientAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
