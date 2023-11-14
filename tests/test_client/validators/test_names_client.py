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
        self.first_name_with_number = {
            'first_name': 'Bruno12',
            'birthday': date(2000, 5, 12)
        }
        self.very_small_first_name = {
            'first_name': 'A',
            'birthday': date(2000, 8, 21)
        }
        self.first_name_valid = {
            'first_name': 'João Rogério',
            'birthday': date(2000, 1, 1)
        }

    def test_first_name_client_with_number_status_code_400(self):
        response = self.client.post(self.url, self.first_name_with_number)
        self.assertEqual(response.status_code, 400)

    def test_client_with_first_name_numeric_not_insert_in_database(self):
        self.client.post(self.url, self.first_name_with_number)
        client = Client.objects.filter(first_name='Bruno12')
        self.assertFalse(client.exists())

    def test_very_small_first_name_of_client_status_code_400(self):
        response = self.client.post(self.url, self.very_small_first_name)
        self.assertEqual(response.status_code, 400)

    def test_very_small_first_name_of_client_not_insert_in_database(self):
        self.client.post(self.url, self.very_small_first_name)
        client = Client.objects.filter(first_name='A')
        self.assertFalse(client.exists())

    def test_first_name_valid_status_code_302(self):
        response = self.client.post(self.url, self.first_name_valid)
        self.assertEqual(response.status_code, 302)

    def test_client_with_first_name_valid_insert_in_database(self):
        self.client.post(self.url, self.first_name_valid)
        client = Client.objects.filter(first_name='João Rogério')
        self.assertTrue(client.exists())

class LastNameClientValidTestCase(TestCase):
    
    def setUp(self) -> None:
        User.objects.create_superuser('SuperUser', password='MyNewPassword')
        self.client.login(username='SuperUser', password='MyNewPassword')
        self.url = reverse('admin:client_client_add')
        self.last_name_with_numbers = {
            'first_name': 'Bruno',
            'last_name': 'L3tr4s e num3r0s',
            'birthday': date(2000, 5, 12)
        }
        self.empty_last_name = {
            'first_name': 'Alessandro',
            'last_name': '',
            'birthday': date(2000, 8, 21)
        }
        self.last_name_valid = {
            'first_name': 'João Rogério',
            'last_name': 'Álvaro Rodrígues',
            'birthday': date(2000, 1, 1)
        }
        self.last_name_very_big = {
            'first_name': 'João Rodrigo',
            'last_name': 'this last name has more than seventy characters resulting in an invalid last name',
            'birthday': date(2000, 1, 1)
        }

    def test_last_name_client_with_numbers_status_code_400(self):
        response = self.client.post(self.url, self.last_name_very_big)
        self.assertEqual(response.status_code, 400)
    
    def test_last_name_client_very_big_status_code_400(self):
        response = self.client.post(self.url, self.last_name_with_numbers)
        self.assertEqual(response.status_code, 400)

    def test_last_name_client_blank_status_code_302(self):
        response = self.client.post(self.url, self.empty_last_name)
        self.assertEqual(response.status_code, 302)

    def test_last_name_client_valid_status_code_302(self):
        response = self.client.post(self.url, self.last_name_valid)
        self.assertEqual(response.status_code, 302)

    def test_last_name_client_with_numbers_not_insert_in_database(self):
        self.client.post(self.url, self.last_name_very_big)
        client = Client.objects.filter(first_name='João Rodrigo')
        self.assertFalse(client.exists())
    
    def test_last_name_client_very_big_not_insert_in_database(self):
        self.client.post(self.url, self.last_name_with_numbers)
        client = Client.objects.filter(first_name='Bruno')
        self.assertFalse(client.exists())

    def test_last_name_client_blank_insert_in_database(self):
        self.client.post(self.url, self.empty_last_name)
        client = Client.objects.filter(first_name='Alessandro')
        self.assertTrue(client.exists())

    def test_last_name_client_valid_insert_in_database(self):
        self.client.post(self.url, self.last_name_valid)
        client = Client.objects.filter(first_name='João Rogério')
        self.assertTrue(client.exists())
