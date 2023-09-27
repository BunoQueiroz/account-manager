from django.test import TestCase
from client.models import Purchase, Client, Account
from product.models import Product, Category
from datetime import datetime


class AccountSumTotalTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client(first_name='Bruno', birthday=datetime.date(datetime.now())).save()
        self.client_in_db = Client.objects.get(first_name='Bruno')

        self.account = Account(client=self.client_in_db).save()
        self.account_in_db = Account.objects.get(client=self.client_in_db)

        self.category = Category(name='Teste').save()
        self.category_in_db = Category.objects.get(name='Teste')
        self.item = Product(
            name = 'Testing',
            price = 100,
            category = self.category_in_db,
            description = 'Sem descrição',
            brand = 'Testes'
        ).save()
        self.item_in_db = Product.objects.get(name='Testing')

        self.purchase_one = Purchase(
            account = self.account_in_db,
            item = self.item_in_db,
            amount = 5
        ).save()
        self.purchase_two = Purchase(
            account = self.account_in_db,
            item = self.item_in_db,
            amount = 18
        ).save()

    def test_sum_total_account_entity(self):
        purchases = Purchase.objects.filter(account=self.account_in_db)
        self.account_in_db.save()
        self.assertEqual(
            self.account_in_db.total,
            sum(purchase.total for purchase in purchases)
        )

