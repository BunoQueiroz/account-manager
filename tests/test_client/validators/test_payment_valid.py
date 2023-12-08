from django.test import TestCase
from client.models import Client, Account
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


class PaymentValidTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('SuperUser', password='MyNewPassword')
        self.client.login(username='SuperUser', password='MyNewPassword')
        self.manager = User.objects.get(username='SuperUser')
        self.url = reverse('admin:client_payment_add')
        Client(first_name='Breno', birthday=date(2000, 8, 21)).save()
        self.client_in_db = Client.objects.get(first_name='Breno')
        self.account = Account.objects.get(client=self.client_in_db)

        self.payment_negative_value = {
            'value': -21,
            'received': self.manager.pk,
            'account': self.account.pk,
            'payer': 'Breno'
        }

    def test_payer_with_negative_value_return_status_code_400(self):
        response = self.client.post(self.url, self.payment_negative_value)
        self.assertEqual(response.status_code, 400)
