from django.test import TestCase
from product.models import Category, Product
from client.models import Client, Account, Purchase
from datetime import datetime
from django.contrib.auth.models import User


class UpdatePurchaseTestCase(TestCase):

    def setUp(self) -> None:
        self.admin_user = User.objects.create_superuser('admin', password='MyPassword')
        self.client.login(username='admin', password='MyPassword')
        self.client_one = Client(first_name='Bruno', birthday=datetime.date(datetime.now())).save()
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
            amount = 1
        ).save()
        self.purchase = Purchase.objects.get(account=self.account_in_db)

        self.data = {'action': 'update', '_selected_action': [self.purchase.pk]}
        self.uri = '/client/purchase/'

    def test_update_purchase_in_admin_site(self):
        self.item_in_db.price = 80
        self.item_in_db.save()
        self.item_in_db.refresh_from_db()
        self.client.post(self.uri, self.data)
        self.purchase.refresh_from_db()
        self.assertEqual(self.purchase.total, 80)

    def test_update_total_account_when_update_purchase(self):
        self.item_in_db.price = 70
        self.item_in_db.save()
        self.item_in_db.refresh_from_db()
        self.client.post(self.uri, self.data)
        self.account_in_db.refresh_from_db()
        self.assertEqual(self.account_in_db.total, 70)
