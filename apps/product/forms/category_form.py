from django.forms import ModelForm
from product.models import Category
from product.forms.validators import name_category_validator


class CategoryModelForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']

    def clean(self):
        name = self.cleaned_data.get('name')
        errors_list = {}
        name_category_validator(name, errors_list)
        if errors_list:
            for error in errors_list:
                error_message = errors_list[error]
                self.add_error(error, error_message)
        return self.cleaned_data
