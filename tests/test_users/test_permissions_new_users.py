from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime


class UserOnlySomePermissionsTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser(username='Bruno', password='MinhaSenha')
        self.client.login(username='Bruno', password='MinhaSenha')

        self.url_add_users = reverse('admin:auth_user_add')
        self.new_user = {
            'username': 'Breno',
            'password': 'OutraSenha',
            'active': True,
            'date_joined_0': date.today(),
            'date_joined_1': datetime.now().strftime('%H:%M:%S'),
        }

    def test_is_possible_create_new_users_in_admin_page(self):
        response = self.client.post(self.url_add_users, self.new_user)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 2)

    def test_new_users_without_access_to_auth_model(self):
        self.client.post(self.url_add_users, self.new_user)
        new_user = User.objects.get(username='Breno')
        list_of_permissions = {
            'client.view_account',
            'client.view_client',
            'client.view_payment',
            'client.view_purchase',
            'product.view_category',
            'product.view_product',
            'client.add_client',
            'client.add_payment',
            'client.add_purchase',
            'product.add_category',
            'product.add_product',
            'client.change_client',
            'client.change_payment',
            'client.change_purchase',
            'product.change_category',
            'product.change_product',
        }
        self.assertEqual(new_user.get_all_permissions(), list_of_permissions)
