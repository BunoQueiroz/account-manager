from django.test import TestCase
from client.models import Account, Client
from datetime import date


class AccountAtributesTestCase(TestCase):

    def setUp(self) -> None:
        Client(
            first_name='Bruno',
            last_name='de Castro',
            cpf='08285054381',
            email='email@gmail.com',
            birthday='2002-08-21'
        ).save()
        self.first_client = Client.objects.get(email='email@gmail.com')

        self.account = Account.objects.get(opened=True)

    def test_atributes_account_class(self):
        self.assertEqual(self.account.client, self.first_client)
        self.assertTrue(self.account.opened)
    
    def test_atributes_account_in_db(self):
        self.assertEqual(self.account.client, self.first_client)
        self.assertTrue(self.account.opened)

    def test_str_method_account_class(self):
        self.assertEqual(
            str(self.account),
            f'Account - {self.account.client.first_name}'
        )

    def test_date_account_instance_auto_now(self):
        self.assertEqual(self.account.opening_date, date.today())
