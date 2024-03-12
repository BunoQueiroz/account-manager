from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class NewUserWithEncriptoPasswordTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('Bryan', password='MyPassword')
        self.client.login(username='Bryan', password='MyPassword')

        self.add_new_user_url = reverse('admin:auth_user_add')
        self.change_user_url = reverse('admin:auth_user_changelist')
        self.data = {
            'username': 'Bruno',
            'password': 'OutraSenha',
            'date_joined_0': date.today(),
            'date_joined_1': datetime.now().strftime('%H:%M:%S'),
        }
        self.data_update = {
            'username': 'Bruno',
            'password': 'OutraSenha',
            'email': '',
            'first_name': 'Bruno',
            'last_name': 'Castro',
            'is_active': True,
            'date_joined_0': date.today(),
            'date_joined_1': datetime.now().strftime('%H:%M:%S'),
            'is_staff': True,
            'is_superuser': True,
        }

    def test_if_is_possible_create_new_users_in_admin_page(self):
        self.client.post(self.add_new_user_url, self.data)
        user = User.objects.filter(username='Bruno')
        self.assertTrue(user.exists())
    
    def test_new_users_via_admin_page_with_encripto_password(self):
        self.client.post(self.add_new_user_url, self.data)
        user = User.objects.filter(username='Bruno').get()
        password = user.password
        regex = r'^pbkdf2_sha256\$600000\$.*=$'
        self.assertRegex(str(password), regex)
    
    def test_update_users_via_admin_page_with_encripto_password(self):
        self.client.post(self.add_new_user_url, self.data)
        user = User.objects.get(username='Bruno')
        self.client.post(f'{self.change_user_url}{user.pk}/change/', self.data_update)
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'Bruno')
        self.assertEqual(user.last_name, 'Castro')
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)
    
    def test_login_new_users_created_via_admin_page(self):
        self.client.post(self.add_new_user_url, self.data)
        user = User.objects.get(username='Bruno')
        self.client.post(f'{self.change_user_url}{user.pk}/change/', self.data_update)
        self.client.logout()
        login = self.client.login(username='Bruno', password='OutraSenha')
        self.assertTrue(login)
