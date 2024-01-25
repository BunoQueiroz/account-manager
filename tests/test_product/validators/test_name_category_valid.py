from django.test import TestCase
from product.models import Category
from django.contrib.auth.models import User
from django.urls import reverse


class NameCategoryValidTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('superuser', password='MyNewPassword')
        self.client.login(username='superuser', password='MyNewPassword')
        self.url = reverse('admin:product_category_add')
        
        self.category_name_with_numbers = {
            'name': 'categ0r1a'
        }
        self.category_name_only_numeric = {
            'name': '12345'
        }
        self.category_name_very_small = {
            'name': 'a'
        }
        self.category_name_very_big = {
            'name': 'categoria com o limite de caracteres excedido alem do normalizado'
        }
        self.category_name_graphic_accents = {
            'name': 'ração'
        }
    
    def test_category_name_with_numbers_return_status_code_400(self):
        response = self.client.post(self.url, self.category_name_with_numbers)
        self.assertEqual(response.status_code, 400)
    
    def test_category_name_only_numeric_return_status_code_400(self):
        response = self.client.post(self.url, self.category_name_only_numeric)
        self.assertEqual(response.status_code, 400)
    
    def test_category_name_very_small_return_status_code_400(self):
        response = self.client.post(self.url, self.category_name_very_small)
        self.assertEqual(response.status_code, 400)
    
    def test_category_name_very_big_return_status_code_400(self):
        response = self.client.post(self.url, self.category_name_very_big)
        self.assertEqual(response.status_code, 400)
    
    def test_category_name_with_graphic_accents_return_status_code_302(self):
        response = self.client.post(self.url, self.category_name_graphic_accents)
        self.assertEqual(response.status_code, 302)


    def test_category_name_with_numbers_not_insert_in_data_base(self):
        self.client.post(self.url, self.category_name_with_numbers)
        category = Category.objects.filter(
            name=self.category_name_with_numbers['name']
        )
        self.assertFalse(category.exists())
    
    def test_category_name_only_numeric_not_insert_in_data_base(self):
        self.client.post(self.url, self.category_name_only_numeric)
        category = Category.objects.filter(
            name=self.category_name_only_numeric['name']
        )
        self.assertFalse(category.exists())
    
    def test_category_name_very_small_not_insert_in_data_base(self):
        self.client.post(self.url, self.category_name_very_small)
        category = Category.objects.filter(
            name=self.category_name_very_small['name']
        )
        self.assertFalse(category.exists())
    
    def test_category_name_very_big_not_insert_in_data_base(self):
        self.client.post(self.url, self.category_name_very_big)
        category = Category.objects.filter(
            name=self.category_name_very_big['name']
        )
        self.assertFalse(category.exists())
    
    def test_category_name_with_graphic_accents_not_insert_in_data_base(self):
        self.client.post(self.url, self.category_name_graphic_accents)
        category = Category.objects.filter(
            name=self.category_name_graphic_accents['name']
        )
        self.assertTrue(category.exists())
