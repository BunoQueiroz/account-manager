from django.forms import ModelForm
from client.models import Payment
from client.forms.payment_validators import value_validator


class PaymentForm(ModelForm):

    class Meta:
        model = Payment
        fields = '__all__'

    def clean(self):
        value = self.data.get('value')
        errors_list = {}
        value_validator(value, errors_list)
        if errors_list:
            for error in errors_list:
                error_message = errors_list[error]
                self.add_error(error, error_message)
        return self.cleaned_data


