from .base_page import BasePage
from selenium.webdriver.common.by import By


title_site = (By.XPATH, '//*[@id="__next"]/div[2]/main/section[1]/h1')
test_email = 'LoVasya33@yandex.ru'
test_password = 'Password1!'
email_form = (By.XPATH, '//input[@placeholder="Введите email"]')
password_form = (By.XPATH, '//input[@placeholder="Введите пароль"]')
button_class = (By.CLASS_NAME, 'MuiButton-containedPrimary')
error_email = (By.CSS_SELECTOR, 'p.css-3zhtyq')
button_register = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div/div/div/a[2]')
reset_password = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div/div/div/a[3]')
email_form_reset = (By.CSS_SELECTOR, 'input[type="email"]')
button_send_email_reset = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div/div/form/button')
complete_send_email_reset = (By.CSS_SELECTOR, 'button.MuiButton-containedPrimary')
menu_button = (By.XPATH, '/html/body/div[1]/div[2]/header/div/div/div[2]/div[1]/button')
logout_button = (By.XPATH, '//*[@id="__next"]/div[2]/header/div/div/div[2]/div[2]/ul/li[6]/a')


class Login(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(url='https://test.startupium.ru/login')
