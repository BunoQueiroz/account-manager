from django.test import TestCase
from client.models import Client, Account, Payment
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


class PaymentPayerValidTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('SuperBruno', password='MyNewPassword')
        self.client.login(username='SuperBruno', password='MyNewPassword')
        self.manager = User.objects.get(username='SuperBruno')
        self.url = reverse('admin:client_payment_add')
        Client(first_name='Bryan', birthday=date(2000, 8, 21)).save()
        self.client_in_db = Client.objects.get(first_name='Bryan')
        self.account = Account.objects.get(client=self.client_in_db)

        self.payment_number_in_payer_name = {
            'value': 30,
            'received': self.manager.pk,
            'account': self.account.pk,
            'payer': 'Ri0'
        }
        self.payment_payer_name_very_small = {
            'value': 30,
            'received': self.manager.pk,
            'account': self.account.pk,
            'payer': 'A'
        }
        self.payment_payer_name_very_long = {
            'value': 30,
            'received': self.manager.pk,
            'account': self.account.pk,
            'payer': 'esse texto comtém mais de cem caracteres para serem utilizandos no teste de validação de quantidade máxima de caracteres'
        }
        self.payment_payer_name_blank = {
            'value': 30,
            'received': self.manager.pk,
            'account': self.account.pk,
            'payer': '    '
        }
        self.payment_payer_name_with_graphics_accents = {
            'value': 30,
            'received': self.manager.pk,
            'account': self.account.pk,
            'payer': 'Rogério Gonçalves'
        }

    def test_payer_with_number_in_payer_name_return_status_code_400(self):
        response = self.client.post(self.url, self.payment_number_in_payer_name)
        self.assertEqual(response.status_code, 400)

    def test_payer_with_payer_very_small_return_status_code_400(self):
        response = self.client.post(self.url, self.payment_payer_name_very_small)
        self.assertEqual(response.status_code, 400)

    def test_payer_with_payer_name_very_long_return_status_code_400(self):
        response = self.client.post(self.url, self.payment_payer_name_very_long)
        self.assertEqual(response.status_code, 400)

    def test_payer_with_payer_name_blank_return_status_code_400(self):
        response = self.client.post(self.url, self.payment_payer_name_blank)
        self.assertEqual(response.status_code, 400)

    def test_payer_with_payer_name_of_graphic_accents_return_status_code_302(self):
        response = self.client.post(
            self.url,
            self.payment_payer_name_with_graphics_accents
        )
        self.assertEqual(response.status_code, 302)

    def test_payer_with_number_in_payer_name_not_insert_in_database(self):
        self.client.post(self.url, self.payment_number_in_payer_name)
        payment = Payment.objects.filter(
            payer=self.payment_number_in_payer_name['payer']
        )
        self.assertFalse(payment.exists())

    def test_payer_with_payer_very_small_not_insert_in_database(self):
        self.client.post(self.url, self.payment_payer_name_very_small)
        payment = Payment.objects.filter(
            payer=self.payment_payer_name_very_small['payer']
        )
        self.assertFalse(payment.exists())

    def test_payer_with_payer_name_very_long_not_insert_in_database(self):
        self.client.post(self.url, self.payment_payer_name_very_long)
        payment = Payment.objects.filter(
            payer=self.payment_payer_name_very_long['payer']
        )
        self.assertFalse(payment.exists())

    def test_payer_with_payer_name_blank_not_insert_in_database(self):
        self.client.post(self.url, self.payment_payer_name_blank)
        payment = Payment.objects.filter(
            payer=self.payment_payer_name_blank['payer']
        )
        self.assertFalse(payment.exists())

    def test_payer_with_payer_name_of_graphic_accents_insert_in_database(self):
        self.client.post(
            self.url,
            self.payment_payer_name_with_graphics_accents
        )
        payment = Payment.objects.filter(
            payer=self.payment_payer_name_with_graphics_accents['payer']
        )
        self.assertTrue(payment.exists())
