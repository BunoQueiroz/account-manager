from django.contrib import admin
from django.http.response import HttpResponse
from product.models import Product, Category
from product.forms import ProductModelForm, CategoryModelForm


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'brand', 'category']
    list_editable = ['brand',]
    search_fields = ['name', 'brand']
    list_filter = ['category', 'brand']
    list_per_page = 30
    form = ProductModelForm
    
    def response_add(self, request, obj, post_url_continue: str | None = ...) -> HttpResponse:
        if self.form.errors:
            HttpResponse.status_code = 400
        return super().response_add(request, obj, post_url_continue)


class CategoryAdmin(admin.ModelAdmin):

    def id_category(self):
        return str(self.pk)[0:8]

    list_display = [id_category, 'name']
    list_editable = ['name']
    search_fields = ['name']
    list_per_page = 30
    form = CategoryModelForm

    def response_add(self, request, obj, post_url_continue: str | None = ...) -> HttpResponse:
        if self.form.errors:
            HttpResponse.status_code = 400
        return super().response_add(request, obj, post_url_continue)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
