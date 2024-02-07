from requests import Session
from dotenv import load_dotenv
import os


load_dotenv()

HOST_TEST = os.getenv('HOST_TEST')
USERNAME_LOGIN = os.getenv('USERNAME_LOGIN')
PASSWORD_LOGIN = os.getenv('PASSWORD_LOGIN')

# Login
url_login = f'http://{HOST_TEST}/login/?next=/'
session = Session()
data_login = {
    'username': f'{USERNAME_LOGIN}',
    'password': f'{PASSWORD_LOGIN}',
    'csrfmiddlewaretoken': session.get(url_login).cookies['csrftoken'],
}
session.post(url_login, data=data_login)

url_client = f'http://{HOST_TEST}/client/client/'
url_product = f'http://{HOST_TEST}/product/product/'


for _ in range(1, 1001):
    session.get(url_client)
    session.get(url_product)
    print(_)
