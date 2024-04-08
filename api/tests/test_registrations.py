import requests

from random import randint
url = 'https://test.startupium.ru/api/'

def test_new_user_registr():
    params = {
        "firstname": f"testapiuser{randint(0,100000)}",
        "lastname": "testapium",
        "email": f"test{randint(0,100000)}apim@mail.ru",
        "password": "secretA!1",
        "password_confirmation": "secretA!1"
        }
    response = requests.post(url=url+'register', params=params)
    assert response.status_code == 201, 'Новый пользователь не создан'

