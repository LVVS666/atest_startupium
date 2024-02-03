import os

from .base_page import BasePage
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

test_email = 'pupok777vasya@gmail.com'
test_password = 'Password1!'
# test_email = os.getenv('email')
# test_password = os.getenv('password')
email_form = (By.XPATH, '//input[@placeholder="Введите email"]')
password_form = (By.XPATH, '//input[@placeholder="Введите пароль"]')
button_class = (By.CLASS_NAME, 'MuiButton-containedPrimary')
error_email = (By.CSS_SELECTOR, 'p.css-3zhtyq')


class Login(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(url='https://startupium.ru/login')
