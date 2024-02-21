from django.test import TestCase
from client.models import Client, Account, Purchase
from product.models import Category, Product
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


class RecalculateAccountTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_superuser('BrunoManager', password='MyPassword')
        self.client.login(username='BrunoManager', password='MyPassword')
        self.admin = User.objects.get(username='BrunoManager')
        
        Client(first_name='MyClient', birthday=date(2002, 8, 21)).save()
        self.client_in_db = Client.objects.get(first_name='MyClient')
        
        self.url_product = reverse('admin:product_product_changelist')
        
        self.account = Account.objects.get(client=self.client_in_db)

        Category(name='MyCategory').save()
        self.my_category = Category.objects.get(name='MyCategory')
        Product(name='MyFirstProduct', price=100, category=self.my_category).save()
        self.my_product = Product.objects.get(name='MyFirstProduct')
        self.new_price = {
            'name': 'MyFirstProduct',
            'price': 110,
            'category': self.my_category.pk
        }

        Purchase(account=self.account, item=self.my_product, amount=1).save()
        self.first_purchase = Purchase.objects.filter(amount=1)

    def test_recalculate_total_after_update_price_of_products(self):
        self.client.post(f'{self.url_product}{self.my_product.pk}/change/', self.new_price)
        self.account.refresh_from_db()
        self.assertEqual(int(self.account.total), 110)
