import time

from page.login import (
    Login,
    email_form,
    password_form,
    button_class,
    test_email,
    test_password,
    error_email, button_register, button_yandex_id_login, yandex_form
)
from page.register import name_page


def test_login(browser):
    '''Проверка удачного логина при валидных данных'''
    login_page = Login(browser)
    login_page.open()
    login_page.wait_element(email_form)
    email = login_page.find(email_form)
    email.send_keys(test_email)
    login_page.wait_element(password_form)
    password = login_page.find(password_form)
    password.send_keys(test_password)
    login_page.wait_element(button_class)
    button = login_page.find(button_class)
    button.click()
    time.sleep(5)
    current_url = login_page.browser.current_url
    assert current_url == 'https://test.startupium.ru/registration', 'Редирект не произошел'


def test_login_email_not_valid(browser):
    '''Проверка логина при невалидном email'''
    login_page = Login(browser)
    login_page.open()
    login_page.wait_element(email_form)
    email = login_page.find(email_form)
    email.send_keys('test@gmail.com')
    login_page.wait_element(password_form)
    password = login_page.find(password_form)
    password.send_keys(test_password)
    login_page.wait_element(button_class)
    button = login_page.find(button_class)
    button.click()
    login_page.wait_element(error_email)
    error_message = login_page.find(error_email)
    assert error_message is not None, 'Уведомления об ошибке не было'


def test_login_password_not_valid(browser):
    '''Проверка логина при невалидном пароле'''
    login_page = Login(browser)
    login_page.open()
    login_page.wait_element(email_form)
    email = login_page.find(email_form)
    email.send_keys(test_email)
    login_page.wait_element(password_form)
    password = login_page.find(password_form)
    password.send_keys('Test_password1!')
    login_page.wait_element(button_class)
    button = login_page.find(button_class)
    button.click()
    login_page.wait_element(error_email)
    error_message = login_page.find(error_email)
    assert error_message is not None, 'Уведомления об ошибке не было'


def test_redirect_register(browser):
    '''Проверка перехода на страницу создания аккаунта'''
    login_page = Login(browser)
    login_page.open()
    login_page.wait_element(button_register)
    button = login_page.find(button_register)
    button.click()
    login_page.wait_element(name_page)
    element_text = login_page.find(name_page)
    assert element_text.text == 'Создание аккаунта', 'Редирект не произошел'

def test_login_in_yandexid(browser):
    '''Тестирование входа через YandexID'''
    login_page = Login(browser)
    login_page.open()
    login_page.wait_element(button_yandex_id_login)
    button = login_page.find(button_yandex_id_login)
    button.click()
    login_page.wait_element(yandex_form)
    yandex_element = login_page.find(yandex_form)
    assert yandex_element is not None, 'Редирект на страницу входа YandexID не произошел'



