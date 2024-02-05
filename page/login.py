from .base_page import BasePage
from selenium.webdriver.common.by import By


test_email = 'pupok777vasya@gmail.com'
test_password = 'Password1!'
email_form = (By.XPATH, '//input[@placeholder="Введите email"]')
password_form = (By.XPATH, '//input[@placeholder="Введите пароль"]')
button_class = (By.CLASS_NAME, 'MuiButton-containedPrimary')
error_email = (By.CSS_SELECTOR, 'p.css-3zhtyq')
button_register = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div/div/div/a[2]')
button_yandex_id_login = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div/div/div/a[1]')
yandex_form = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/form/div[1]/div[1]/h1')


class Login(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(url='https://test.startupium.ru/login')
