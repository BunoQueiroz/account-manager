from django.test import TestCase
from product.models import Product, Category
from django.contrib.auth.models import User
from django.urls import reverse


class PriceProductValidTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('superuser', password='MyNewPassword')
        self.client.login(username='superuser', password='MyNewPassword')
        self.url = reverse('admin:product_product_add')
        self.category = Category(name='MyCategory').save()
        self.category_in_db = Category.objects.get(name='MyCategory')

        self.price_of_type_str = {
            'name': 'MyProduct',
            'category': self.category_in_db.pk,
            'price': '1.5'
        }
        self.price_alphanumeric = {
            'name': 'MyOutherProduct',
            'category': self.category_in_db.pk,
            'price': 'price1'
        }
        self.price_of_type_int = {
            'name': 'MoreProduct',
            'category': self.category_in_db.pk,
            'price': 1
        }
        self.price_with_comma = {
            'name': 'OutherProduct',
            'category': self.category_in_db.pk,
            'price': '1,2'
        }

    def test_product_with_price_of_type_str_only_numeric_return_status_302(self):
        response = self.client.post(self.url, self.price_of_type_str)
        self.assertEqual(response.status_code, 302)
    
    def test_product_with_price_alphanumeric_return_status_400(self):
        response = self.client.post(self.url, self.price_alphanumeric)
        self.assertEqual(response.status_code, 400)
        
    def test_product_with_price_of_type_int_return_status_302(self):
        response = self.client.post(self.url, self.price_of_type_int)
        self.assertEqual(response.status_code, 302)
    
    def test_product_with_price_with_comma_return_status_302(self):
        response = self.client.post(self.url, self.price_with_comma)
        self.assertEqual(response.status_code, 400)


    def test_product_with_price_of_type_str_only_numeric_insert_in_database(self):
        self.client.post(self.url, self.price_of_type_str)
        product = Product.objects.filter(name='MyProduct')
        self.assertTrue(product.exists())
    
    def test_product_with_price_alphanumeric_not_insert_in_database(self):
        self.client.post(self.url, self.price_alphanumeric)
        product = Product.objects.filter(name='MyOutherProduct')
        self.assertFalse(product.exists())
        
    def test_product_with_price_of_type_int_insert_in_database(self):
        self.client.post(self.url, self.price_of_type_int)
        product = Product.objects.filter(name='MoreProduct')
        self.assertTrue(product.exists())
    
    def test_product_with_price_with_comma_not_insert_in_database(self):
        self.client.post(self.url, self.price_with_comma)
        product = Product.objects.filter(name='OutherProduct')
        self.assertFalse(product.exists())

