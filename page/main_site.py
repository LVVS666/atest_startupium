from .base_page import BasePage
from selenium.webdriver.common.by import By

from .login import Login, email_form, password_form, button_class

title = (By.CLASS_NAME, 'css-1lv0diq')
create_command = (By.XPATH, '//*[@id="__next"]/div[2]/main/section[1]/div/a[1]')
search_project = (By.XPATH, '//*[@id="__next"]/div[2]/main/section[1]/div/a[2]')
title_new_project = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div/h2')
title_search_project = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/form/div/div[1]/div/span')
title_search_users = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/form/div/div[1]/div/span')
projects = (By.XPATH, '//a[@href="/projects"]')
users = (By.XPATH, '//a[@href="/users"]')


class MainSite(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(url='https://test.startupium.ru')

    def open_auth(self):
        login_page = Login(self.browser)
        login_page.open()
        login_page.wait_element(email_form)
        email = login_page.find(email_form)
        email.send_keys('pupok777vasya@gmail.com')
        login_page.wait_element(password_form)
        password = login_page.find(password_form)
        password.send_keys('Password1!')
        login_page.wait_element(button_class)
        button = login_page.find(button_class)
        button.click()