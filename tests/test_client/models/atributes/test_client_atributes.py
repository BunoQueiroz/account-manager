from django.test import TestCase
from client.models import Client
from datetime import date


class ClientAtributesTestCase(TestCase):
    
    def setUp(self) -> None:
        self.client = Client(
            first_name='Bruno',
            last_name='de Castro Queiroz',
            cpf='08285054381',
            email='bruno@gmail.com',
            birthday='2002-08-21'
        )
        self.client.save()
        self.client_in_db = Client.objects.get(email='bruno@gmail.com')
        
    def test_atributes_class_client(self):
        self.assertEqual(self.client.first_name, 'Bruno')
        self.assertEqual(self.client.last_name, 'de Castro Queiroz')
        self.assertEqual(self.client.cpf, '08285054381')
        self.assertEqual(self.client.email, 'bruno@gmail.com')
        self.assertEqual(self.client.birthday, '2002-08-21')
        
    def test_atributes_class_client_in_db(self):
        
        self.assertEqual(self.client_in_db.first_name, 'Bruno')
        self.assertEqual(self.client_in_db.last_name, 'de Castro Queiroz')
        self.assertEqual(self.client_in_db.cpf, '08285054381')
        self.assertEqual(self.client_in_db.email, 'bruno@gmail.com')
        self.assertEqual(self.client_in_db.birthday, date(2002, 8, 21))

    def test_str_method_client_class(self):
        self.assertEqual(
            str(self.client_in_db),
            f'{self.client_in_db.first_name} {self.client_in_db.last_name}'
        )

    def test_date_register_today_for_new_clients(self):
        self.assertEqual(self.client_in_db.register_date, date.today())
