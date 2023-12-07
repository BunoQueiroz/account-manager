from django.test import TestCase
from product.models import Product, Category
from django.contrib.auth.models import User
from django.urls import reverse


class DescriptionProductValidTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('superuser', password='MyNewPassword')
        self.client.login(username='superuser', password='MyNewPassword')
        self.url = reverse('admin:product_product_add')
        self.category = Category(name='MyCategory').save()
        self.category_in_db = Category.objects.get(name='MyCategory')

        self.description_blank = {
            'name': 'MyProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': 'Brand valid',
            'description': ''
        }
        self.description_with_only_numbers = {
            'name': 'MyProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': 'Brand valid',
            'description': '21322131651'
        }
        self.description_with_numbers_initial = {
            'name': 'MyProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': 'Brand valid',
            'description': '21322131651 com letras'
        }
        self.description_not_string_format = {
            'name': 'MyProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': 'Brand valid',
            'description': 213221
        }
        self.description_very_long = {
            'name': 'MyProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': 'Brand valid',
            'description': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Asperiores ipsam assumenda adipisci amet sapiente sed nisi laborum sunt temporibus, cum inventore hic repudiandae pariatur iure quae ducimus sint ab? Praesentium!'
        }
        self.description_very_small = {
            'name': 'MyProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': 'Brand valid',
            'description': 'i'
        }
        self.description_with_special_characters = {
            'name': 'MyProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': 'Brand valid',
            'description': 'Minha descr!ção T$M C@RACT&R&S &SP&C!@!$'
        }
    
    def test_product_with_description_blank_return_status_code_302(self):
        response = self.client.post(self.url, self.description_blank)
        self.assertEqual(response.status_code, 302)
    
    def test_product_with_description_with_numbers_initial_return_status_code_302(self):
        response = self.client.post(self.url, self.description_with_numbers_initial)
        self.assertEqual(response.status_code, 302)
    
    def test_product_with_description_with_special_characters_return_status_code_302(self):
        response = self.client.post(self.url, self.description_with_special_characters)
        self.assertEqual(response.status_code, 302)

    def test_product_with_description_with_only_numbers_return_status_code_400(self):
        response = self.client.post(self.url, self.description_with_only_numbers)
        self.assertEqual(response.status_code, 400)
    
    def test_product_with_description_not_string_format_return_status_code_400(self):
        response = self.client.post(self.url, self.description_not_string_format)
        self.assertEqual(response.status_code, 400)
    
    def test_product_with_description_very_long_return_status_code_400(self):
        response = self.client.post(self.url, self.description_very_long)
        self.assertEqual(response.status_code, 400)
    
    def test_product_with_description_very_small_return_status_code_400(self):
        response = self.client.post(self.url, self.description_very_small)
        self.assertEqual(response.status_code, 400)
    
    def test_product_with_description_blank_insert_in_database(self):
        self.client.post(self.url, self.description_blank)
        product = Product.objects.filter(description='')
        self.assertTrue(product.exists())
    
    def test_product_with_description_with_numbers_initial_insert_in_database(self):
        self.client.post(self.url, self.description_with_numbers_initial)
        product = Product.objects.filter(description='21322131651 com letras')
        self.assertTrue(product.exists())
    
    def test_product_with_description_with_special_characters_insert_in_database(self):
        self.client.post(self.url, self.description_with_special_characters)
        product = Product.objects.filter(description='Minha descr!ção T$M C@RACT&R&S &SP&C!@!$')
        self.assertTrue(product.exists())

    def test_product_with_description_with_only_numbers_not_insert_in_database(self):
        self.client.post(self.url, self.description_with_only_numbers)
        product = Product.objects.filter(description='21322131651')
        self.assertFalse(product.exists())
    
    def test_product_with_description_not_string_format_not_insert_in_database(self):
        self.client.post(self.url, self.description_not_string_format)
        product = Product.objects.filter(description=213221)
        self.assertFalse(product.exists())
    
    def test_product_with_description_very_long_not_insert_in_database(self):
        self.client.post(self.url, self.description_very_long)
        product = Product.objects.filter(
            description='Lorem ipsum dolor, sit amet consectetur adipisicing elit. Asperiores ipsam assumenda adipisci amet sapiente sed nisi laborum sunt temporibus, cum inventore hic repudiandae pariatur iure quae ducimus sint ab? Praesentium!'
        )
        self.assertFalse(product.exists())
    
    def test_product_with_description_very_small_not_insert_in_database(self):
        self.client.post(self.url, self.description_very_small)
        product = Product.objects.filter(description='i')
        self.assertFalse(product.exists())
