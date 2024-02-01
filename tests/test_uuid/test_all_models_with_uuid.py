from django.test import TestCase
from client.models import Account, Client, Payment, Purchase
from product.models import Category, Product
from datetime import date
from django.contrib.auth.models import User


class ClientModelsWithUUIDTestCase(TestCase):

    def setUp(self):

        self.uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}$'
        
        User.objects.create_superuser('Bruno', password='MyPassword')
        self.superuser = User.objects.get(username='Bruno')

        Client(first_name='Brenda', birthday=date(2000, 8, 21)).save()
        self.client_in_db = Client.objects.get(first_name='Brenda')
        
        self.account = Account.objects.get(client=self.client_in_db.pk)

        Category(name='MyCategory').save()
        self.category = Category.objects.get(name='MyCategory')

        Product(name='MyProduct', price=10, category=self.category).save()
        self.product = Product.objects.get(name='MyProduct')

        Purchase(account=self.account, amount=1, item=self.product).save()
        self.purchase = Purchase.objects.get(account=self.account)

        Payment(value=10, account=self.account, received=self.superuser, payer='Brenda').save()
        self.payment = Payment.objects.get(payer='Brenda')

    def test_client_model_have_pk_in_uuid_format(self):
        pk_client = str(self.client_in_db.pk)
        self.assertRegex(pk_client, self.uuid_pattern)

    def test_account_model_have_pk_in_uuid_format(self):
        pk_account = str(self.account.pk)
        self.assertRegex(pk_account, self.uuid_pattern)

    def test_category_model_have_pk_in_uuid_format(self):
        pk_category = str(self.category.pk)
        self.assertRegex(pk_category, self.uuid_pattern)

    def test_product_model_have_pk_in_uuid_format(self):
        pk_product = str(self.product.pk)
        self.assertRegex(pk_product, self.uuid_pattern)

    def test_purchase_model_have_pk_in_uuid_format(self):
        pk_purchase = str(self.purchase.pk)
        self.assertRegex(pk_purchase, self.uuid_pattern)

    def test_payment_model_have_pk_in_uuid_format(self):
        pk_payment = str(self.payment.pk)
        self.assertRegex(pk_payment, self.uuid_pattern)
