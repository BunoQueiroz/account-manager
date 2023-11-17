from django.test import TestCase
from product.models import Product, Category
from django.contrib.auth.models import User
from django.urls import reverse


class NameProductValidTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('superuser', password='MyNewPassword')
        self.client.login(username='superuser', password='MyNewPassword')
        self.url = reverse('admin:product_product_add')
        self.category = Category(name='MyCategory').save()
        self.category_in_db = Category.objects.get(name='MyCategory')

        self.name_with_special_character = {
            'name': 'n@m&',
            'category': self.category_in_db.pk,
            'price': 1.5
        }
        self.name_with_many_letters = {
            'name': 'esse-nome-deve-possuir-mais-de-setenta-carateres-para-o-teste-ocorrer-de-forma-correta',
            'category': self.category_in_db.pk,
            'price': 1.5
        }
        self.name_with_few_letters = {
            'name': 'A',
            'category': self.category_in_db.pk,
            'price': 1.7
        }
        self.name_with_numbers = {
            'name': 'The n4m3',
            'category': self.category_in_db.pk,
            'price': 1.5
        }
        self.name_with_hyphen = {
            'name': 'nome Com - é válido',
            'category': self.category_in_db.pk,
            'price': 2.0
        }
        
    def test_name_product_with_special_characters_return_status_code_400(self):
        response = self.client.post(self.url, self.name_with_special_character)
        self.assertEqual(response.status_code, 400)

    def test_name_product_with_many_letters_return_status_code_400(self):
        response = self.client.post(self.url, self.name_with_many_letters)
        self.assertEqual(response.status_code, 400)

    def test_name_product_with_few_letters_not_return_status_code_302(self):
        response = self.client.post(self.url, self.name_with_few_letters)
        self.assertNotEqual(response.status_code, 302)
    
    def test_name_product_with_numbers_return_status_code_302(self):
        response = self.client.post(self.url, self.name_with_numbers)
        self.assertEqual(response.status_code, 302)
    
    def test_name_product_with_hypen_return_status_code_302(self):
        response = self.client.post(self.url, self.name_with_hyphen)
        self.assertEqual(response.status_code, 302)


    def test_name_product_with_special_characters_not_insert_in_database(self):
        self.client.post(self.url, self.name_with_special_character)
        product = Product.objects.filter(name='n@m&')
        self.assertFalse(product.exists())

    def test_name_product_with_many_letters_not_insert_in_database(self):
        self.client.post(self.url, self.name_with_many_letters)
        product = Product.objects.filter(
            name='esse-nome-deve-possuir-mais-de-setenta-carateres-para-o-teste-ocorrer-de-forma-correta'
        )
        self.assertFalse(product.exists())

    def test_name_product_with_few_letters_not_insert_in_database(self):
        self.client.post(self.url, self.name_with_few_letters)
        product = Product.objects.filter(name='A')
        self.assertFalse(product.exists())
    
    def test_name_product_with_numbers_insert_in_database(self):
        self.client.post(self.url, self.name_with_numbers)
        product = Product.objects.filter(name='The n4m3')
        self.assertTrue(product.exists())
    
    def test_name_product_with_hypen_insert_in_database(self):
        self.client.post(self.url, self.name_with_hyphen)
        product = Product.objects.filter(name='nome Com - é válido')
        self.assertTrue(product.exists())

