import time
import allure
import requests

from page.login import email_form
from page.main_site import MainSite, title, create_command, title_new_project, search_project, title_search_project, \
    projects, users, title_search_users, title_about, about

@allure.feature('Общая проверка главной страницы')
@allure.story('Проверка статус года главной страницы')
def test_status_code():
    '''Проверка статус кода главной страницы'''
    with allure.step("Запрос отправлен, посмотрим код ответа"):
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


def test_search_project(browser):
    '''Проверка кнопки "Найти команду"'''
    page = MainSite(browser)
    page.open()
    page.wait_element(search_project)
    button_search = page.find(search_project)
    button_search.click()
    page.wait_element(title_search_project)
    assert page.find(title_search_project).text == 'Поиск проектов', 'Редирект не произошел'


def test_projects(browser):
    '''Проверка кнопки "Проекты" в хедере'''
    page = MainSite(browser)
    page.open()
    page.wait_element(projects)
    button_projects = page.find(projects)
    page.browser.execute_script('arguments[0].click()', button_projects)
    page.wait_element(title_search_project)
    assert page.find(title_search_project).text == 'Поиск проектов', 'Редирект не произошел'


def test_users(browser):
    '''Проверка кнопки "Пользователи" в хедере'''
    page = MainSite(browser)
    page.open()
    page.wait_element(users)
    button_users = page.find(users)
    page.browser.execute_script('arguments[0].click()', button_users)
    page.wait_element(title_search_users)
    assert page.find(title_search_users).text == 'Поиск пользователей', 'Редирект не произошел'

def test_about_site(browser):
    '''Проверка кнопки "О сайте" в хедере'''
    page = MainSite(browser)
    page.open()
    page.wait_element(about)
    button_about = page.find(about)
    page.browser.execute_script('arguments[0].click()', button_about)
    page.wait_element(title_about)
    assert page.find(title_about).text in 'Startupium\nплатформа объединяющая\nлюдей', 'Редирект не произошел'