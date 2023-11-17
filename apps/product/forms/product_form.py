from django.forms import ModelForm
from product.models import Product
from product.forms.validators import name_product_validator


class ProductModelForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        name = self.cleaned_data.get('name')
        errors_list = {}
        name_product_validator(name, errors_list)
        if errors_list:
            for error in errors_list:
                error_message = errors_list[error]
                self.add_error(error, error_message)
        return self.cleaned_data

