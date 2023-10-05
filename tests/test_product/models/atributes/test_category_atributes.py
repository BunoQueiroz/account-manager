from django.test import TestCase
from product.models import Category


class CategoryAtributesTestCase(TestCase):

    def setUp(self) -> None:
        self.category = Category(name='Frios')
        self.category.save()
        self.category_in_db = Category.objects.get(name='Frios')

    def test_atributes_category_class(self):
        self.assertEqual(self.category.name, 'Frios')

    def test_str_method_of_category_class(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_atributes_category_in_db(self):
        self.assertEqual(self.category_in_db.name, 'Frios')
