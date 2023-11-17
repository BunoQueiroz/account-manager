from django.contrib import admin
from django.http.response import HttpResponse
from product.models import Product, Category
from product.forms import ProductModelForm


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'brand', 'category']
    list_editable = ['name', 'description', 'price']
    search_fields = ['name', 'brand']
    list_filter = ['brand', 'category']
    form = ProductModelForm
    
    def response_add(self, request, obj, post_url_continue: str | None = ...) -> HttpResponse:
        if self.form.errors:
            HttpResponse.status_code = 400
        return super().response_add(request, obj, post_url_continue)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
