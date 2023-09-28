from django.test import TestCase
from client.models import Purchase, Client, Account
from product.models import Product, Category
from datetime import datetime


class PurchaseAtributesTestCase(TestCase):

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

        self.purchase = Purchase(
            account = self.account_in_db,
            item = self.item_in_db,
            amount = 5
        )
    
    def test_atributes_purchase_class(self):
        self.assertEqual(self.purchase.account, self.account_in_db)
        self.assertEqual(self.purchase.item, self.item_in_db)
        self.assertEqual(self.purchase.amount, 5)

    def test_atributes_purchase_class_in_db(self):
        self.purchase.save()
        purchase_in_db = Purchase.objects.get(account=self.account_in_db)        
        self.assertEqual(purchase_in_db.account, self.account_in_db)
        self.assertEqual(purchase_in_db.item, self.item_in_db)
        self.assertEqual(purchase_in_db.amount, self.purchase.amount)
        self.assertEqual(purchase_in_db.moment, self.purchase.moment)
        
    def test_total_value_purchase(self):
        self.purchase.save()
        purchase_in_db = Purchase.objects.get(account=self.account_in_db)
        self.assertEqual(
            purchase_in_db.total,
            self.purchase.amount * self.purchase.item.price
        )

    def test_str_method_of_purchase_class(self):
        self.purchase.save()
        purchase_in_db = Purchase.objects.get(account=self.account_in_db)
        self.assertEqual(
            str(purchase_in_db),
            f'{self.purchase.account.client.first_name} - {self.purchase.moment.date()}'
        )
