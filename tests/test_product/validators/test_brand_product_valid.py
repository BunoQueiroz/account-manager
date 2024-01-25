from django.test import TestCase
from product.models import Product, Category
from django.contrib.auth.models import User
from django.urls import reverse


class BrandProductValidTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('superuser', password='MyNewPassword')
        self.client.login(username='superuser', password='MyNewPassword')
        self.url = reverse('admin:product_product_add')
        self.category = Category(name='MyCategory').save()
        self.category_in_db = Category.objects.get(name='MyCategory')

        self.brand_very_small = {
            'name': 'MyProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': 'B'
        }
        self.brand_very_many = {
            'name': 'MyOutherProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': 'Mais que cinquenta caracteres para o teste ocorrer corretamente'
        }
        self.brand_blank = {
            'name': 'OutherProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': ''
        }
        self.brand_with_numbers = {
            'name': 'OutherProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': '3 coracoes'
        }
        self.brand_only_numbers = {
            'name': 'OutherProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': '12345000'
        }
        self.brand_with_special_characters = {
            'name': 'OutherProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': 'M! & Br@nd'
        }
        self.brand_with_graphic_accents = {
            'name': 'OutherProduct',
            'category': self.category_in_db.pk,
            'price': 1.5,
            'brand': 'Maratá Betânia Coração'
        }

    def test_product_of_brand_very_small_return_status_400(self):
        response = self.client.post(self.url, self.brand_very_small)
        self.assertEqual(response.status_code, 400)

    def test_product_of_brand_very_many_return_status_400(self):
        response = self.client.post(self.url, self.brand_very_many)
        self.assertEqual(response.status_code, 400)

    def test_product_of_brand_only_numeric_return_status_400(self):
        response = self.client.post(self.url, self.brand_only_numbers)
        self.assertEqual(response.status_code, 400)

    def test_product_of_brand_with_special_characters_return_status_400(self):
        response = self.client.post(self.url, self.brand_with_special_characters)
        self.assertEqual(response.status_code, 400)

    def test_product_of_brand_blank_return_status_302(self):
        response = self.client.post(self.url, self.brand_blank)
        self.assertEqual(response.status_code, 302)

    def test_product_of_brand_with_numbers_return_status_302(self):
        response = self.client.post(self.url, self.brand_with_numbers)
        self.assertEqual(response.status_code, 302)

    def test_product_of_brand_with_graphic_accents_return_status_302(self):
        response = self.client.post(self.url, self.brand_with_graphic_accents)
        self.assertEqual(response.status_code, 302)


    def test_product_of_brand_very_small_not_insert_in_data_base(self):
        self.client.post(self.url, self.brand_very_small)
        product = Product.objects.filter(brand='B')
        self.assertFalse(product.exists())

    def test_product_of_brand_very_many_not_insert_in_data_base(self):
        self.client.post(self.url, self.brand_very_many)
        product = Product.objects.filter(
            brand='Mais que cinquenta caracteres para o teste ocorrer corretamente'
        )
        self.assertFalse(product.exists())

    def test_product_of_brand_only_numeric_not_insert_in_data_base(self):
        self.client.post(self.url, self.brand_only_numbers)
        product = Product.objects.filter(brand='12345000')
        self.assertFalse(product.exists())

    def test_product_of_brand_with_special_characters_not_insert_in_data_base(self):
        self.client.post(self.url, self.brand_with_special_characters)
        product = Product.objects.filter(brand='M! & Br@nd')
        self.assertFalse(product.exists())
        
    def test_product_of_brand_blank_insert_in_data_base(self):
        self.client.post(self.url, self.brand_blank)
        product = Product.objects.filter(brand='')
        self.assertTrue(product.exists())

    def test_product_of_brand_with_numbers_insert_in_data_base(self):
        self.client.post(self.url, self.brand_with_numbers)
        product = Product.objects.filter(brand='3 coracoes')
        self.assertTrue(product.exists())

    def test_product_of_brand_with_graphic_accents_insert_in_data_base(self):
        self.client.post(self.url, self.brand_with_graphic_accents)
        product = Product.objects.filter(brand='Maratá Betânia Coração')
        self.assertTrue(product.exists())

