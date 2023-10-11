from django.test import TestCase
from product.models import Category, Product


class ProductPriceTestCase(TestCase):

    def setUp(self) -> None:
        Category.objects.create(name='TestPrice')
        self.category = Category.objects.get(name='TestPrice')
        Product.objects.create(
            name='Testing', price=0.7, category=self.category
        )
        self.product = Product.objects.filter(name='Testing')

    def test_price_float_is_valid(self):
        register_product = self.product.exists()
        self.assertTrue(register_product)

    def test_price_is_float_in_data_base(self):
        price_product = self.product.get().price
        self.assertEqual(price_product, 0.7)
        