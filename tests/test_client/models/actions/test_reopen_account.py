from django.test import TestCase
from client.models import Client, Account
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


class ReopenAccountTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('BrunoManager', password='MyPassword')
        self.client.login(username='BrunoManager', password='MyPassword')
        Client.objects.create(first_name='Bruno', birthday=datetime.today())
        self.client_in_db = Client.objects.get(first_name='Bruno')
        
        self.account = Account.objects.get(client=self.client_in_db)
        
        self.path_delete_account = '/client/account/'
        self.path_reopen_account = '/client/client/'

        self.data_delete = {
            'action': 'delete_selected',
            '_selected_action': [self.account.pk],
            'post': 'yes',
        }
        self.data_reopen = {
            'action': 'reopen_account',
            '_selected_action': [self.client_in_db.pk],
        }

    def test_reopen_account_with_client_register(self):
        self.client.post(self.path_delete_account, self.data_delete)
        self.client.post(self.path_reopen_account, self.data_reopen)

        reopened_account = Account.objects.filter(client=self.client_in_db).exists()
        self.assertTrue(reopened_account)
        
