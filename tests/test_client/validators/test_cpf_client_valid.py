from django.test import TestCase
from client.models import Client
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


class FirstNameClientValidTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('SuperUser', password='MyNewPassword')
        self.client.login(username='SuperUser', password='MyNewPassword')
        self.url = reverse('admin:client_client_add')
        self.cpf_with_letters = {
            'first_name': 'Bruno',
            'birthday': date(2000, 5, 12),
            'cpf': 'myc9f'
        }
        self.cpf_very_short = {
            'first_name': 'Breno',
            'birthday': date(2000, 8, 21),
            'cpf':'0878468152'
        }
        self.cpf_very_long = {
            'first_name': 'Bred',
            'birthday': date(2000, 1, 1),
            'cpf': '805214125326'
        }
        self.valid_cpf_with_punctuation = {
            'first_name': 'Bryan',
            'birthday': date(2000, 1, 1),
            'cpf': '959.287.670-30'
        }
        self.valid_cpf_without_punctuation = {
            'first_name': 'Brunno',
            'birthday': date(2000, 1, 1),
            'cpf': '08541007090'
        }


    def test_cpf_with_letters_status_400(self):
        response = self.client.post(self.url, self.cpf_with_letters)
        self.assertEqual(response.status_code, 400)
    
    def test_cpf_very_short_status_400(self):
        response = self.client.post(self.url, self.cpf_very_short)
        self.assertEqual(response.status_code, 400)
    
    def test_cpf_very_long_status_400(self):
        response = self.client.post(self.url, self.cpf_very_long)
        self.assertEqual(response.status_code, 400)
    
    def test_valid_cpf_with_punctuation_status_302(self):
        response = self.client.post(self.url, self.valid_cpf_with_punctuation)
        self.assertEqual(response.status_code, 302)
    
    def test_valid_cpf_without_punctuation_status_302(self):
        response = self.client.post(self.url, self.valid_cpf_without_punctuation)
        self.assertEqual(response.status_code, 302)
    
     
    def test_cpf_with_letters_not_insert_in_database(self):
        self.client.post(self.url, self.cpf_with_letters)
        client = Client.objects.filter(first_name='Bruno')
        self.assertFalse(client.exists())
    
    def test_cpf_very_short_not_insert_in_database(self):
        self.client.post(self.url, self.cpf_very_short)
        client = Client.objects.filter(first_name='Breno')
        self.assertFalse(client.exists())
    
    def test_cpf_very_long_not_insert_in_database(self):
        self.client.post(self.url, self.cpf_very_long)
        client = Client.objects.filter(first_name='Bred')
        self.assertFalse(client.exists())
    
    def test_valid_cpf_with_punctuation_insert_in_database(self):
        self.client.post(self.url, self.valid_cpf_with_punctuation)
        client = Client.objects.filter(first_name='Bryan')
        self.assertTrue(client.exists())
    
    def test_valid_cpf_without_punctuation_insert_in_database(self):
        self.client.post(self.url, self.valid_cpf_without_punctuation)
        client = Client.objects.filter(first_name='Brunno')
        self.assertTrue(client.exists())
    
