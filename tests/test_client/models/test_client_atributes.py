from django.test import TestCase
from client.models import Client
from datetime import date


class ClientAtributesTestCase(TestCase):
    
    def setUp(self) -> None:
        self.client_atributes = Client(
            first_name='Bruno',
            last_name='de Castro Queiroz',
            cpf='08285054381',
            email='bruno@gmail.com',
            birthday='2002-08-21'
        )
        return super().setUp()
    
    def test_atributes_class_client(self):
        self.assertEqual(self.client_atributes.first_name, 'Bruno')
        self.assertEqual(self.client_atributes.last_name, 'de Castro Queiroz')
        self.assertEqual(self.client_atributes.cpf, '08285054381')
        self.assertEqual(self.client_atributes.email, 'bruno@gmail.com')
        self.assertEqual(self.client_atributes.birthday, '2002-08-21')
        
    def test_atributes_class_client_in_db(self):
        self.client_atributes.save()
        client = Client.objects.get(email='bruno@gmail.com')
        
        self.assertEqual(client.first_name, 'Bruno')
        self.assertEqual(client.last_name, 'de Castro Queiroz')
        self.assertEqual(client.cpf, '08285054381')
        self.assertEqual(client.email, 'bruno@gmail.com')
        self.assertEqual(client.birthday, date(2002, 8, 21))
        
