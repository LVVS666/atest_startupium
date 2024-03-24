import time
import allure
import requests

from selenium.webdriver.common.keys import Keys
from page.search_projects import SearchProjectsSite, form_search, search_tag, method_search, button_search, name_project


@allure.feature('Запрос HTTP')
@allure.title('Проверка статус кода страницы "Проекты')
def test_projects_status_code():
    with allure.step("Запрос отправлен, проверка кода ответа"):
        response = requests.get('https://test.startupium.ru/projects')
        assert response.status_code == 200, f'Ошибка получен статус: {response.status_code}'


@allure.feature('Поиск проектов')
@allure.title('Поиск по названию ')
def test_search_projects_at_name(browser):
    page_projects = SearchProjectsSite(browser)
    page_projects.open()
    page_projects.wait_element(form_search)
    page_projects.wait_element(method_search)
    method_button = page_projects.find(method_search)
    with allure.step('Выбрать метод поиска: По тэгу'):
        page_projects.browser.execute_script('arguments[0].click()', method_button)
    page_projects.wait_element(search_tag)
    tag_button = page_projects.find(search_tag)
    page_projects.browser.execute_script('arguments[0].click()', tag_button)
    tag = page_projects.find(form_search)
    with allure.step('Ввести в поисковую строку тэг "PHP"'):
        tag.send_keys('PHP')
    tag.send_keys(Keys.ENTER)
    with allure.step('Нажать кнопку поиска'):
        page_projects.find(button_search).click()
    page_projects.wait_element(name_project)
    assert page_projects.find(name_project), 'Поиск по тэгу отработал некорректно'

