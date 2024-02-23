from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from faker import Faker

from product.models import Product, Category
from client.models import (
    Client,
    Account,
    Payment,
    Purchase
)


class MaxClientsObjectsPerPageTestCase(TestCase):

    def setUp(self) -> None:
        
        faker = Faker()

        User.objects.create_superuser('bruno', password='mypassword')
        self.client.login(username='bruno', password='mypassword')

        for _ in range(26):
            Client(first_name=faker.unique.first_name(), birthday=faker.date(end_datetime='-19y')).save()

        self.url = reverse('admin:client_client_changelist')

    def test_check_if_have_only_25_clients_per_page_in_admin_site(self):
        if Client.objects.count() > 25:
            response = self.client.get(self.url)
            pattern = r'data-actions-icnt="25"'
            self.assertRegex(str(response.content), pattern)
        else:
            self.fail("Quantidade de CLIENTES inapropriada para o teste de limitação de objetos por página!")


class MaxAccountsObjectsPerPageTestCase(TestCase):

    def setUp(self) -> None:
        
        faker = Faker()

        User.objects.create_superuser('bruno', password='mypassword')
        self.client.login(username='bruno', password='mypassword')

        for _ in range(26):
            Client(first_name=faker.unique.first_name(), birthday=faker.date(end_datetime='-19y')).save()

        self.url = reverse('admin:client_account_changelist')

    def test_check_if_have_only_25_accounts_per_page_in_admin_site(self):
        if Account.objects.count() > 25:
            response = self.client.get(self.url)
            pattern = r'data-actions-icnt="25"'
            self.assertRegex(str(response.content), pattern)
        else:
            self.fail("Quantidade de CONTAS inapropriada para o teste de limitação de objetos por página!")


class MaxPaymentsObjectsPerPageTestCase(TestCase):

    def setUp(self) -> None:
        
        faker = Faker()

        User.objects.create_superuser('bruno', password='mypassword')
        self.my_superuser = User.objects.get(username='bruno')
        self.client.login(username='bruno', password='mypassword')

        Client(first_name='Bruno', birthday=faker.date(end_datetime='-19y')).save()
        self.client_test = Client.objects.get(first_name='Bruno')

        self.my_account = Account.objects.get(client=self.client_test)

        for _ in range(31):
            Payment(
                value=faker.random_int(1, 10),
                received=self.my_superuser,
                account=self.my_account,
                payer=faker.unique.first_name()
            ).save()

        self.url = reverse('admin:client_payment_changelist')

    def test_check_if_have_only_30_payments_per_page_in_admin_site(self):
        if Payment.objects.count() > 30:
            response = self.client.get(self.url)
            pattern = r'data-actions-icnt="30"'
            self.assertRegex(str(response.content), pattern)
        else:
            self.fail("Quantidade de PAGAMENTOS inapropriada para o teste de limitação de objetos por página!")


class MaxPurchasesObjectsPerPageTestCase(TestCase):

    def setUp(self) -> None:
        
        faker = Faker()

        User.objects.create_superuser('bruno', password='mypassword')
        self.client.login(username='bruno', password='mypassword')

        Category(name='MyCategoryTest').save()
        self.category = Category.objects.get(name='MyCategoryTest')

        Product(name='My Product', price=5, category=self.category).save()
        self.product = Product.objects.get(name='My Product')

        Client(first_name='Brenos', birthday=faker.date(end_datetime='-19y')).save()
        self.client_test = Client.objects.get(first_name='Brenos')
        self.account = Account.objects.get(client=self.client_test)

        for _ in range(31):
            Purchase(
                account=self.account,
                item=self.product,
                amount=4
            ).save()

        self.url = reverse('admin:client_purchase_changelist')

    def test_check_if_have_only_30_purchases_per_page_in_admin_site(self):
        if Purchase.objects.count() > 30:
            response = self.client.get(self.url)
            pattern = r'data-actions-icnt="30"'
            self.assertRegex(str(response.content), pattern)
        else:
            self.fail("Quantidade de COMPRAS inapropriada para o teste de limitação de objetos por página!")
