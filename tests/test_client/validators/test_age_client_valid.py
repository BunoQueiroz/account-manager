from django.test import TestCase
from client.models import Client
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


class AgeClientValidTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('superuser', password='MyNewPassword')
        self.client.login(username='superuser', password='MyNewPassword')
        self.url = reverse('admin:client_client_add')
        self.client_under_18 = {
            'first_name': 'BrunoTest',
            'birthday': date(2010, 5, 12)
        }
        self.client_with_more_18 = {
            'first_name': 'MyNameIsBruno',
            'birthday': date(2000, 8, 21)
        }

    def test_age_client_under_18_years_status_code_400(self):
        response = self.client.post(self.url, self.client_under_18)
        self.assertEqual(response.status_code, 400)

    def test_age_client_not_valid_insert_in_database(self):
        self.client.post(self.url, self.client_under_18)
        client = Client.objects.filter(first_name='BrunoTest')
        self.assertFalse(client.exists())

    def test_age_client_with_more_18_years_status_code_201(self):
        response = self.client.post(self.url, self.client_with_more_18)
        self.assertEqual(response.status_code, 302)

    def test_age_client_valid_insert_in_database(self):
        self.client.post(self.url, self.client_with_more_18)
        client = Client.objects.filter(first_name='MyNameIsBruno')
        self.assertTrue(client.exists())

        