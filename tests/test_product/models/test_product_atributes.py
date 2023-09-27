from django.test import TestCase
from product.models import Product, Category
from datetime import datetime


class ProductAtributesTestCase(TestCase):

    def setUp(self) -> None:
        self.first_category = Category(
            name='Massas',
        )
        self.first_category.save()
        self.category = Category.objects.get(name='Massas')
        self.product = Product(
            name='Pacote de pão',
            price=7,
            criation_date='2023-09-22',
            category=self.category,
            description='No momento, sem descrição',
            brand='Sem marca'
        )
        self.product.save()

    def test_atributes_product_class(self):
        self.assertEqual(self.product.name, 'Pacote de pão')
        self.assertEqual(self.product.price, 7)
        self.assertEqual(self.product.criation_date, datetime.date(datetime.now()))
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.description, 'No momento, sem descrição')
        self.assertEqual(self.product.brand, 'Sem marca')

    def test_atributes_product_class_in_db(self):
        product = Product.objects.get(name='Pacote de pão')
        self.assertEqual(product.name, 'Pacote de pão')
        self.assertEqual(product.price, 7)
        self.assertEqual(product.criation_date, datetime.date(datetime.now()))
        self.assertEqual(product.category, self.category)
        self.assertEqual(product.description, 'No momento, sem descrição')
        self.assertEqual(product.brand, 'Sem marca')
