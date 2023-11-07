from django.test import TestCase
from client.models import Client
from datetime import datetime
from django.contrib.auth.models import User
import re
from django.urls import reverse


class SearchAccountTestCase(TestCase):

    def setUp(self) -> None:
        self.admin_user = User.objects.create_superuser('admin', password='MyPassword')
        self.client.login(username='admin', password='MyPassword')
        self.client_one = Client(first_name='Bruno', birthday=datetime.date(datetime.now())).save()
        self.url = reverse('admin:client_account_changelist')

    def test_status_code_for_search_in_accounts_page(self):
        response = self.client.get(f'{self.url}?q=br')
        self.assertEqual(response.status_code, 200)


class OrderingAccountTestCase(TestCase):

    def setUp(self) -> None:
        self.admin_user = User.objects.create_superuser('admin', password='MyPassword')
        self.client.login(username='admin', password='MyPassword')
        self.client_one = Client(first_name='Bruno', birthday=datetime.date(datetime.now())).save()
        self.client_one = Client(first_name='Pedro', birthday=datetime.date(datetime.now())).save()
        self.client_one = Client(first_name='Breno', birthday=datetime.date(datetime.now())).save()
        self.url = reverse('admin:client_account_changelist')
        
    def test_ordering_accounts_by_first_name_of_clients(self):
        response = self.client.get(f'{self.url}?o=1')
        pattern = r'/*[B,P][e,d,r,u,n]{3}[o]'
        accounts = re.findall(pattern, str(response.content)) # search for 'Pedro' and 'Bruno' in their respective order
        list_true = ['Breno', 'Bruno', 'Pedro']
        self.assertListEqual(accounts, list_true)
    
    def test_reverse_ordering_accounts_by_first_name_of_clients(self):
        response = self.client.get(f'{self.url}?o=-1')
        pattern = r'/*[B,P][e,d,r,u,n]{3}[o]'
        accounts = re.findall(pattern, str(response.content))
        list_true = ['Pedro', 'Bruno', 'Breno']
        self.assertListEqual(accounts, list_true)
