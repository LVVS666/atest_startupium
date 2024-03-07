import time

import allure
import requests

from page.login import (
    Login,
    email_form,
    password_form,
    button_class,
    test_email,
    test_password,
    error_email, button_register, reset_password, email_form_reset, button_send_email_reset, complete_send_email_reset,
    menu_button, logout_button
)

from page.register import name_page


@allure.feature('Запрос HTTP')
@allure.story('Проверка статус года страницы логина')
def test_status_code():
    with allure.step("Запрос отправлен, проверка кода ответа"):
        response = requests.get('https://test.startupium.ru/login')
        assert response.status_code == 200, f'Ошибка получен статус: {response.status_code}'


@allure.feature('Логин с валидными данными')
@allure.story('Проверка удачного логина при валидных данных')
def test_login(browser):
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
    with allure.step("Все поля заполнены валидными данными,ожидается редирект"):
        current_url = login_page.browser.current_url
        assert current_url == 'https://test.startupium.ru/registration', 'Редирект не произошел'


@allure.feature('Логин с невалидными данными')
@allure.story('Проверка логина при невалидном email')
def test_login_email_not_valid(browser):
    login_page = Login(browser)
    login_page.open()
    login_page.wait_element(email_form)
    email = login_page.find(email_form)
    with allure.step("Введен невалидный email"):
        email.send_keys('notvalide_test@gmail.com')
    login_page.wait_element(password_form)
    password = login_page.find(password_form)
    password.send_keys(test_password)
    login_page.wait_element(button_class)
    button = login_page.find(button_class)
    button.click()
    with allure.step("Попытка входа при невалидном email и получение ошибки"):
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


def test_button_reset_password(browser):
    '''Проверка кнопки сброса пароля '''
    login_page = Login(browser)
    login_page.open()
    login_page.wait_element(reset_password)
    button_reset = login_page.find(reset_password)
    button_reset.click()
    login_page.wait_element(email_form_reset)
    form_email = login_page.find(email_form_reset)
    assert form_email is not None, 'Кнопка сброса пароля не работает.'


def test_reset_password(browser):
    '''Проверка сброса пароля и отправка сообщения на почту'''
    login_page = Login(browser)
    login_page.open()
    login_page.wait_element(reset_password)
    button_reset = login_page.find(reset_password)
    button_reset.click()
    login_page.wait_element(email_form_reset)
    form_email = login_page.find(email_form_reset)
    form_email.send_keys(test_email)
    login_page.wait_element(button_send_email_reset)
    button_send_email = login_page.find(button_send_email_reset)
    button_send_email.click()
    login_page.wait_element(complete_send_email_reset)
    message = login_page.find(complete_send_email_reset)
    assert message is not None, 'Сообщение по сбросу пароля на почту не отправляется'

def test_logout(browser):
    '''Проверка логаута и редиректа на главную страницу'''
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
    login_page.browser.execute_script('arguments[0].click()', button)
    login_page.wait_element(menu_button)
    menu = login_page.find(menu_button)
    login_page.browser.execute_script('arguments[0].click()', menu)
    login_page.wait_element(logout_button)
    logout = login_page.find(logout_button)
    login_page.browser.execute_script('arguments[0].click()', logout)
    url_logout = 'https://test.startupium.ru'
    assert url_logout in login_page.browser.current_url, 'Выход не произошел'

