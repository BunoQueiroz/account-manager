from django.test import TestCase
from client.models import Client, Account
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


class CreateAccountTestCase(TestCase):

    def setUp(self) -> None:
        self.admin = User.objects.create_superuser('Bruno', password='MyPassword')
        self.client.login(username='Bruno', password='MyPassword')

        self.path = reverse('admin:client_client_add')
        self.data = {
            'first_name': 'Bruno',
            'birthday': date(2002, 8, 21)
        }

    def test_create_account_when_insert_new_client(self):
        self.client.post(self.path, self.data)
        client_test = Client.objects.get(first_name='Bruno')
        account = Account.objects.filter(client=client_test).exists()
        self.assertTrue(account)
