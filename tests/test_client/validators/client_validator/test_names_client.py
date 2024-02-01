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
        self.first_name_very_small = {
            'first_name': 'A',
            'birthday': date(2000, 8, 21)
        }
        self.first_name_with_graphic_accents = {
            'first_name': 'Conceição Guíta',
            'birthday': date(2000, 1, 1)
        }

    def test_first_name_client_with_number_status_code_400(self):
        response = self.client.post(self.url, self.first_name_with_number)
        self.assertEqual(response.status_code, 400)

    def test_very_small_first_name_of_client_status_code_400(self):
        response = self.client.post(self.url, self.first_name_very_small)
        self.assertEqual(response.status_code, 400)

    def test_first_name_valid_status_code_302(self):
        response = self.client.post(self.url, self.first_name_with_graphic_accents)
        self.assertEqual(response.status_code, 302)

    def test_client_with_first_name_numeric_not_insert_in_database(self):
        self.client.post(self.url, self.first_name_with_number)
        client = Client.objects.filter(first_name='Bruno12')
        self.assertFalse(client.exists())

    def test_very_small_first_name_of_client_not_insert_in_database(self):
        self.client.post(self.url, self.first_name_very_small)
        client = Client.objects.filter(first_name='A')
        self.assertFalse(client.exists())

    def test_client_with_first_name_valid_insert_in_database(self):
        self.client.post(self.url, self.first_name_with_graphic_accents)
        client = Client.objects.filter(first_name='Conceição Guíta')
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
        self.last_name_blank = {
            'first_name': 'Alessandro',
            'last_name': '',
            'birthday': date(2000, 8, 21)
        }
        self.last_name_with_graphic_accents = {
            'first_name': 'João Rogério',
            'last_name': 'Álvaro Rodrígues da Conceição',
            'birthday': date(2000, 1, 1)
        }
        self.last_name_very_big = {
            'first_name': 'João Rodrigo',
            'last_name': 'this last name has more than seventy characters resulting in an invalid last name',
            'birthday': date(2000, 1, 1)
        }
        self.last_name_limit_characters = {
            'first_name': 'Rodrygo',
            'last_name': 'this last name is the maximum size allowed for validation true',
            'birthday': date(2000, 1, 1)
        }

    def test_last_name_client_with_numbers_status_code_400(self):
        response = self.client.post(self.url, self.last_name_with_numbers)
        self.assertEqual(response.status_code, 400)
    
    def test_last_name_client_blank_status_code_302(self):
        response = self.client.post(self.url, self.last_name_blank)
        self.assertEqual(response.status_code, 302)

    def test_last_name_client_graphic_accents_status_code_302(self):
        response = self.client.post(self.url, self.last_name_with_graphic_accents)
        self.assertEqual(response.status_code, 302)

    def test_last_name_client_very_big_status_code_400(self):
        response = self.client.post(self.url, self.last_name_very_big)
        self.assertEqual(response.status_code, 400)

    def test_last_name_client_limit_characters_status_code_302(self):
        response = self.client.post(self.url, self.last_name_limit_characters)
        self.assertEqual(response.status_code, 302)


    def test_last_name_client_with_numbers_not_insert_in_database(self):
        self.client.post(self.url, self.last_name_with_numbers)
        client = Client.objects.filter(first_name='João Rodrigo')
        self.assertFalse(client.exists())

    def test_last_name_client_blank_insert_in_database(self):
        self.client.post(self.url, self.last_name_blank)
        client = Client.objects.filter(first_name='Alessandro')
        self.assertTrue(client.exists())
    
    def test_last_name_client_graphic_accents_insert_in_database(self):
        self.client.post(self.url, self.last_name_with_graphic_accents)
        client = Client.objects.filter(first_name='João Rogério')
        self.assertTrue(client.exists())

    def test_last_name_client_very_big_not_insert_in_database(self):
        self.client.post(self.url, self.last_name_very_big)
        client = Client.objects.filter(first_name='João Rodrigo')
        self.assertFalse(client.exists())

    def test_last_name_client_limit_characters_insert_in_database(self):
        self.client.post(self.url, self.last_name_limit_characters)
        client = Client.objects.filter(first_name='Rodrygo')
        self.assertTrue(client.exists())
