import time

import requests

from page.login import email_form
from page.main_site import MainSite, title, create_command, title_new_project


def test_status_code():
    '''Проверка статус кода главной страницы'''
    response = requests.get('https://test.startupium.ru/')
    assert response.status_code == 200, f'Ошибка получен статус: {response.status_code}'


def test_main_title(browser):
    '''Проверка заголовка на главной странице'''
    page = MainSite(browser)
    page.open()
    page.wait_element(title)
    title_text = page.find(title)
    assert title_text.text == 'Startupium', 'На главной странице неверный заголовок'


def test_create_command_not_auth(browser):
    '''Проверка кнопки "Создать команду" без авторизации'''
    page = MainSite(browser)
    page.open()
    page.wait_element(create_command)
    button_command = page.find(create_command)
    button_command.click()
    time.sleep(5)
    page.wait_element(email_form)
    assert page.find(email_form), 'Редирект не произошел'


def test_create_command_auth(browser):
    '''Проверка кнопки "Создать команду" c авторизацией'''
    page = MainSite(browser)
    page.open_auth()
    page.wait_element(create_command)
    button_command = page.find(create_command)
    button_command.click()
    time.sleep(5)
    page.wait_element(title_new_project)
    assert page.find(title_new_project).text == 'Новый проект', 'Редирект не произошел'
