from requests import Session


# Login
url_login = 'http://localhost/login/?next=/'
session = Session()
data_login = {
    'username': 'root',
    'password': 'bruno',
    'csrfmiddlewaretoken': session.get(url_login).cookies['csrftoken'],
}
session.post(url_login, data=data_login)

url_client = 'http://localhost/client/client/'
url_product = 'http://localhost/product/product/'


for _ in range(1, 1001):
    session.get(url_client)
    session.get(url_product)
    print(_)
