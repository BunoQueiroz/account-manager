from django.test import TestCase
from client.models import Client, Account, Payment
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


class PaymentValueValidTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('SuperUser', password='MyNewPassword')
        self.client.login(username='SuperUser', password='MyNewPassword')
        self.manager = User.objects.get(username='SuperUser')
        self.url = reverse('admin:client_payment_add')
        Client(first_name='Breno', birthday=date(2000, 8, 21)).save()
        self.client_in_db = Client.objects.get(first_name='Breno')
        self.account = Account.objects.get(client=self.client_in_db)

        self.payment_decimal_numbers_in_value = {
            'value': 3.141592,
            'received': self.manager.pk,
            'account': self.account.pk,
            'payer': 'Breno'
        }
        self.payment_string_format_in_value = {
            'value': '32',
            'received': self.manager.pk,
            'account': self.account.pk,
            'payer': 'Breno'
        }
        self.payment_negative_value = {
            'value': -21,
            'received': self.manager.pk,
            'account': self.account.pk,
            'payer': 'Breno'
        }
        self.payment_with_string_in_value = {
            'value': '32s',
            'received': self.manager.pk,
            'account': self.account.pk,
            'payer': 'Breno'
        }
        self.payment_only_character_in_value = {
            'value': 'nots',
            'received': self.manager.pk,
            'account': self.account.pk,
            'payer': 'Breno'
        }

    def test_payer_with_decimal_numbers_in_value_return_status_code_302(self):
        response = self.client.post(self.url, self.payment_decimal_numbers_in_value)
        self.assertEqual(response.status_code, 302)

    def test_payer_with_string_format_in_value_return_status_code_302(self):
        response = self.client.post(self.url, self.payment_string_format_in_value)
        self.assertEqual(response.status_code, 302)

    def test_payer_with_negative_value_return_status_code_400(self):
        response = self.client.post(self.url, self.payment_negative_value)
        self.assertEqual(response.status_code, 400)

    def test_payer_with_string_in_value_return_status_code_400(self):
        response = self.client.post(self.url, self.payment_with_string_in_value)
        self.assertEqual(response.status_code, 400)

    def test_payer_only_character_in_value_return_status_code_400(self):
        response = self.client.post(self.url, self.payment_only_character_in_value)
        self.assertEqual(response.status_code, 400)

    def test_payer_with_decimal_numbers_in_value_insert_in_database(self):
        self.client.post(self.url, self.payment_decimal_numbers_in_value)
        payment = Payment.objects.filter(
            value=self.payment_decimal_numbers_in_value['value']
        )
        self.assertTrue(payment.exists())

    def test_payer_with_string_format_in_value_insert_in_database(self):
        self.client.post(self.url, self.payment_string_format_in_value)
        payment = Payment.objects.filter(
            value=self.payment_string_format_in_value['value']
        )
        self.assertTrue(payment.exists())
    
    def test_payer_with_negative_value_not_insert_in_database(self):
        self.client.post(self.url, self.payment_negative_value)
        payment = Payment.objects.filter(
            value=self.payment_negative_value['value']
        )
        self.assertFalse(payment.exists())
