from django.test import TestCase
from client.models import Client, Account, Payment, Purchase
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
        
        self.url_payments = reverse('admin:client_payment_changelist')
        self.url_purchase = reverse('admin:client_purchase_changelist')
        
        self.account = Account.objects.get(client=self.client_in_db)

        Category(name='MyCategory').save()
        self.my_category = Category.objects.get(name='MyCategory')
        Product(name='MyFirstProduct', price=100, category=self.my_category).save()
        self.my_product = Product.objects.get(name='MyFirstProduct')

        Purchase(account=self.account, item=self.my_product, amount=1).save()
        self.first_purchase = Purchase.objects.filter(amount=1)
        Purchase(account=self.account, item=self.my_product, amount=3).save()
        self.second_purchase = Purchase.objects.filter(amount=3)

        Payment(value=10, received=self.admin, account=self.account, payer='Breno').save()
        self.payment = Payment.objects.filter(payer='Breno')

    def test_recalculate_total_after_delete_any_payment(self):
        self.client.post(f'{self.url_payments}{self.payment.get().pk}/delete/', {'post': 'yes'})
        self.account.refresh_from_db()
        self.assertEqual(self.account.total, 400)

    def test_recalculate_total_after_delete_any_purchase(self):
        self.client.post(f'{self.url_purchase}{self.first_purchase.get().pk}/delete/', {'post': 'yes'})
        self.account.refresh_from_db()
        self.assertEqual(self.account.total, 290)
