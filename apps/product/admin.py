from django.contrib import admin
from product.models import Product, Category

@admin.action(description='update')
def update(modeladmin, request, queryset):
    for item in queryset:
        item.save()

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'brand', 'category']
    list_editable = ['name', 'description', 'price']
    search_fields = ['name', 'brand']
    list_filter = ['brand', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.add_action(update)
