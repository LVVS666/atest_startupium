import os
import http

from test_api.mvp.request_model import Response
from dotenv import load_dotenv

load_dotenv()

users_response = Response(f"{os.getenv('BASE_URL')}/users")


def test_status_code_get_users():
    response_status_code = users_response.get_request().status_code
    assert response_status_code == http.HTTPStatus.OK, f'Ожидаемый статус код: {http.HTTPStatus.OK}' \
                                                       f'Полученный статус код:{response_status_code}' \
                                                       f'Проблема с доступом к пользователям'
def test_status_code_get_user():
    users_response.base_url = users_response.base_url + '/178'
    response_status_code = users_response.get_request().status_code
    assert response_status_code == http.HTTPStatus.OK, f'Ожидаемый статус код: {http.HTTPStatus.OK}' \
                                                       f'Полученный статус код:{response_status_code}' \
                                                       f'Проблема с доступом к пользователю c id 178'