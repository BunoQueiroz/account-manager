from django.forms import ModelForm
from client.models import Client
from .client_validators import *


class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = '__all__'

    def clean(self):
        birthday = self.cleaned_data.get('birthday')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        cpf = self.cleaned_data.get('cpf')
        errors_list = {}
        min_age(birthday, 18, errors_list)
        first_name_validator(first_name, errors_list)
        last_name_validator(last_name, errors_list)
        cpf_validator(cpf, errors_list)
        if errors_list:
            for error in errors_list:
                error_message = errors_list[error]
                self.add_error(error, error_message)
        return self.cleaned_data
