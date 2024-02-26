from requests import Session
from faker import Faker
from dotenv import load_dotenv
import os


load_dotenv()

HOST_TEST = os.getenv('HOST_TEST')
USERNAME_LOGIN = os.getenv('USERNAME_LOGIN')
PASSWORD_LOGIN = os.getenv('PASSWORD_LOGIN')
CATEGORY_ID = os.getenv('CATEGORY_ID')


# Login
url_login = f'http://{HOST_TEST}/login/?next=/'
session = Session()
data_login = {
    'username': f'{USERNAME_LOGIN}',
    'password': f'{PASSWORD_LOGIN}',
    'csrfmiddlewaretoken': session.get(url_login).cookies['csrftoken'],
}
session.post(url_login, data=data_login)


# Post New client
def post_new_client():
    url_new_client = f'http://{HOST_TEST}/client/client/add/'

    faker = Faker()

    new_client = {
        'first_name': faker.unique.first_name(),
        'last_name': faker.last_name(),
        'cpf': '',
        'email': '',
        'birthday': faker.date(),
        'csrfmiddlewaretoken': session.get(url_new_client).cookies['csrftoken'],
    }
    session.post(url_new_client, data=new_client)

# Post New Product
def post_new_product():
    url_new_product = f'http://{HOST_TEST}/product/product/add/'

    faker = Faker()

    new_product = {
        'name': faker.bothify(text='Product ????????'),
        'price': faker.random_int(min=1, max=150),
        'category': {CATEGORY_ID},
        'description': faker.text(),
        'brand': faker.lexify(text='??????????', letters='ABCDEFG'),
        'csrfmiddlewaretoken': session.get(url_new_product).cookies['csrftoken'],
    }
    session.post(url_new_product, data=new_product)

for _ in range(1, 201):
    post_new_product()
    post_new_client()
    print(_)
