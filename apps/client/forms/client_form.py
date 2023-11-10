from django.forms import ModelForm
from client.models import Client
from .validators import min_age


class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = '__all__'

    def clean(self):
        birthday = self.cleaned_data.get('birthday')
        errors_list = {}
        min_age(birthday, 18, errors_list)
        if errors_list:
            for error in errors_list:
                error_message = errors_list[error]
                self.add_error(error, error_message)
        return self.cleaned_data
