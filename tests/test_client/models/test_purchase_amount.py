from django.test import TestCase
from client.models import Client, Account, Purchase
from product.models import Category, Product


class PurchaseAmountTestCase(TestCase):

    def setUp(self) -> None:
        Category.objects.create(name='category')
        self.category = Category.objects.get(name='category')
        
        Product.objects.create(
            name='product', price=3, category=self.category
        )
        self.product = Product.objects.get(name='product')

        Client.objects.create(first_name='Bruno', birthday='2002-08-21')
        self.client_test = Client.objects.get(first_name='Bruno')
        self.account = Account.objects.get(client=self.client_test)

        Purchase.objects.create(
            account=self.account,
            item=self.product,
            amount=0.9,
        )
        self.purchase = Purchase.objects.filter(account=self.account)

    def test_purchase_acept_float_value_in_amount(self):
        self.assertTrue(self.purchase.exists())

    def test_purchase_total_with_float_value_in_amount(self):
        total_of_purchase = self.purchase.get().total
        self.assertEqual(total_of_purchase, 2.7)
