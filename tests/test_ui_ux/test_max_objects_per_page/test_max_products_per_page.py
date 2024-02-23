from django.test import TestCase
from django.contrib.auth.models import User
from faker import Faker
from product.models import Product, Category
from django.urls import reverse


class MaxProductsObjectsPerPageTestCase(TestCase):

    def setUp(self) -> None:
        
        faker = Faker()

        User.objects.create_superuser('bruno', password='mypassword')
        self.client.login(username='bruno', password='mypassword')

        Category(name='MyCategoryTest').save()
        self.category = Category.objects.get(name='MyCategoryTest')

        for _ in range(31):
            self.new_product = Product(
                name=faker.bothify(text='Product ????????'),
                price=faker.random_int(min=1, max=150),
                category=self.category,
                description=faker.text(),
                brand=faker.lexify(text='??????????', letters='ABCDEFG')
            ).save()

        self.url = reverse('admin:product_product_changelist')

    def test_check_if_have_only_30_products_per_page_in_admin_site(self):
        if Product.objects.count() > 30:
            response = self.client.get(self.url)
            pattern = r'data-actions-icnt="30"'
            self.assertRegex(str(response.content), pattern)
        else:
            self.fail("Quantidade de PRODUTOS inapropriada para o teste de limitação de objetos por página!")


class MaxCategorysObjectsPerPageTestCase(TestCase):

    def setUp(self) -> None:
        
        faker = Faker()

        User.objects.create_superuser('bruno', password='mypassword')
        self.client.login(username='bruno', password='mypassword')

        for _ in range(31):
            self.new_product = Category(
                name=faker.bothify(text='Category ????????'),
            ).save()

        self.url = reverse('admin:product_category_changelist')

    def test_check_if_have_only_30_categorys_per_page_in_admin_site(self):
        if Category.objects.count() > 30:
            response = self.client.get(self.url)
            pattern = r'data-actions-icnt="30"'
            self.assertRegex(str(response.content), pattern)
        else:
            self.fail("Quantidade de CATEGORIAS inapropriada para o teste de limitação de objetos por página!")
