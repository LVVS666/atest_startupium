from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    '''Базовый класс страниц'''
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        '''Поиск элемента'''
        return self.browser.find_element(*args)

    def wait_element(self, selector, time=10):
        '''Ожидания появления элемента на странице'''
        WebDriverWait(self.browser, time).until(
            EC.presence_of_element_located(selector))
