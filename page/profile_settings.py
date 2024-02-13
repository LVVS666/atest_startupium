from .base_page import BasePage
from page.login import test_email, test_password, Login, email_form, password_form, button_class
from selenium.webdriver.common.by import By

position_form = (By.XPATH, '//*[@id=":rb:"]')
warrning_position_form = (By.XPATH, '//*[@id=":rb:-helper-text"]')
warrning_position_form_leng = (By.XPATH, '//*[@id=":rb:-helper-text"]')


class ProfileSetting(BasePage):
    '''Класс страницы настроек профиля'''
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        login_page = Login(self.browser)
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



