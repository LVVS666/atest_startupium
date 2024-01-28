import pytest
import requests

from dotenv import load_dotenv
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



load_dotenv()


class TestAuth:

    test_name = 'Test_name'
    test_email = 'Test_email@gmail.ru'
    test_password = 'Password1!'

    @pytest.fixture()
    def browser_activate(self, request):
        browser = Chrome()

        def browser_deactivate():
            browser.quit()
        request.addfinalizer(browser_deactivate)
        return browser


    def test_status_code(self):
        '''Проверка ответа сервера == 200'''
        response = requests.get('https://startupium.ru/create-account')
        assert response.status_code == 200, f'Ошибка получен статус: {response.status_code}'

    def test_open_site(self, browser_activate):
        '''Поиск элемента "Создание аккаунта"'''
        browser_activate.get(url='https://startupium.ru/create-account')
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h3.MuiTypography-root.MuiTypography-h3.css-1ea1e2g')))

        element = browser_activate.find_element(By.CSS_SELECTOR, 'h3.MuiTypography-root.MuiTypography-h3.css-1ea1e2g')
        assert element.text == 'Создание аккаунта', 'Текст на странице не соответствует'

    def test_form_name(self, browser_activate):
        '''Проверка наличия поля ввода имени'''
        browser_activate.get('https://startupium.ru/create-account')
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Введите имя"]')))
        element_name = browser_activate.find_element(By.XPATH, '//input[@placeholder="Введите имя"]')
        assert element_name.get_attribute('placeholder') == 'Введите имя', 'Поле ввода имени отсутствует'

    def test_form_email(self, browser_activate):
        '''Проверка наличия поля ввода email'''
        browser_activate.get('https://startupium.ru/create-account')
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Введите email"]')))
        element_email = browser_activate.find_element(By.XPATH, '//input[@placeholder="Введите email"]')
        assert element_email.get_attribute('placeholder') == 'Введите email', 'Поле ввода email отсутствует'

    def test_form_password(self, browser_activate):
        '''Проверка наличия поля ввода пароля'''
        browser_activate.get('https://startupium.ru/create-account')
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Придумайте пароль"]')))
        element_password1 = browser_activate.find_element(By.XPATH, '//input[@placeholder="Придумайте пароль"]')
        assert element_password1.get_attribute('placeholder') == 'Придумайте пароль', 'Поле ввода пароля отсутствует'

    def test_form_repeat_password(self, browser_activate):
        '''Проверка налчия поля повторного ввода пароля'''
        browser_activate.get('https://startupium.ru/create-account')
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Повторите пароль"]')))
        element_password2 = browser_activate.find_element(By.XPATH, '//input[@placeholder="Повторите пароль"]')
        assert element_password2.get_attribute('placeholder') == 'Повторите пароль', 'Поле повтора пароля отсутствует'

    def test_search_button(self, browser_activate):
        '''Проверка наличия кнопки подтверждения регистрации'''
        browser_activate.get('https://startupium.ru/create-account')
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Повторите пароль"]')))
        button = browser_activate.find_element(By.CLASS_NAME, 'MuiButton-containedPrimary')
        assert button is not None, 'Кнопка подтверждения регистрации отсутствует'


    def test_all_form_not_name(self, browser_activate):
        '''Проверка незаполненного поля имени'''
        browser_activate.get('https://startupium.ru/create-account')
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Введите email"]')))
        element_email = browser_activate.find_element(By.XPATH, '//input[@placeholder="Введите email"]')
        element_email.send_keys(self.test_email)
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Придумайте пароль"]')))
        element_password1 = browser_activate.find_element(By.XPATH, '//input[@placeholder="Придумайте пароль"]')
        element_password1.send_keys(self.test_password)
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Повторите пароль"]')))
        element_password2 = browser_activate.find_element(By.XPATH, '//input[@placeholder="Повторите пароль"]')
        element_password2.send_keys(self.test_password)
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Повторите пароль"]')))
        button = browser_activate.find_element(By.CLASS_NAME, 'MuiButton-containedPrimary')
        button.click()
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Обязательно для заполнения')]")))
        message_element = browser_activate.find_element(By.XPATH, "//p[contains(text(), 'Обязательно для заполнения')]")
        assert message_element is not None, 'Сообщение о незаполненном поле имени не появилось'

    def test_all_form_not_email(self, browser_activate):
        '''Проверка незаполненного поля имени'''
        browser_activate.get('https://startupium.ru/create-account')
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Введите имя"]')))
        element_name = browser_activate.find_element(By.XPATH, '//input[@placeholder="Введите имя"]')
        element_name.send_keys(self.test_name)
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Придумайте пароль"]')))
        element_password1 = browser_activate.find_element(By.XPATH, '//input[@placeholder="Придумайте пароль"]')
        element_password1.send_keys(self.test_password)
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Повторите пароль"]')))
        element_password2 = browser_activate.find_element(By.XPATH, '//input[@placeholder="Повторите пароль"]')
        element_password2.send_keys(self.test_password)
        WebDriverWait(browser_activate, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Повторите пароль"]')))
        button = browser_activate.find_element(By.CLASS_NAME, 'MuiButton-containedPrimary')
        button.click()
        WebDriverWait(browser_activate, 10).until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, "//span[contains(text(), 'Обязательно для заполнения')]")))
        form_elements = browser_activate.find_element(By.XPATH, "//span[contains(text(), 'Обязательно для заполнения')]")
        assert form_elements is not None, 'Сообщение о незаполненном поле email не появилось'



