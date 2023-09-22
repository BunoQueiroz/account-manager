from django.test import TestCase
from apps.product.models import Product, Category


'''class ProductAtributesTestCase(TestCase):

    def setUp(self) -> None:
        print('cuida-'*5)
        self.first_category = Category(
            name='Massas',
        )
        self.first_category.save()
        self.category = Category.objects.get(name='Massas')
        print(self.category)
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
        self.assertEqual(self.product.criation_date, '2023-09-22')
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.description, 'No momento, sem descrição')
        self.assertEqual(self.product.brand, 'Sem marca')
'''