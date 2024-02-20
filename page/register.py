from .base_page import BasePage
from selenium.webdriver.common.by import By


complete_register = (By.CSS_SELECTOR, 'h2.MuiTypography-root.MuiTypography-h2.css-1cabzw6')
name_page = (By.CSS_SELECTOR, 'h3.MuiTypography-root.MuiTypography-h3.css-1ea1e2g')
name_form_path = (By.XPATH, '//input[@placeholder="Введите имя"]')
email_form_path = (By.XPATH, '//input[@placeholder="Введите email"]')
password_form_path = (By.XPATH, '//input[@placeholder="Придумайте пароль"]')
password_repeat_path = (By.XPATH, '//input[@placeholder="Повторите пароль"]')
button_class = (By.CLASS_NAME, 'MuiButton-containedPrimary')
warning_form_not_leng_name = (By.XPATH, "//p[contains(text(), 'Минимум 3 символа')]")
warning_form_path_name = (By.XPATH, "//p[contains(text(), 'Обязательно для заполнения')]")
warning_form_path = (By.XPATH, "//span[contains(text(), 'Обязательно для заполнения')]")
warning_form_password_number = (By.XPATH, "//span[contains(text(), 'Должен содержать не менее одной цифры.')]")
warning_form_password_lenght = (By.XPATH, "//span[contains(text(), 'Должен содержать не менее одной прописной латинской буквы.')]")
warning_form_password_sybmol = (By.XPATH, "//span[contains(text(), 'Должен содержать не менее одного специального символа.')]")
warning_form_not_password = (By.XPATH, "//span[contains(text(), 'Пароли не совпадают.')]")
warning_not_register = (By.CSS_SELECTOR, 'p.css-3zhtyq')


class Register(BasePage):
    '''Класс страницы регистрации'''
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(url='https://test.startupium.ru/create-account')


