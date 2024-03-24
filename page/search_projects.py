from .base_page import BasePage
from selenium.webdriver.common.by import By

name_project = (By.XPATH, '//h2[text()="TEST"]')
form_search = (By.XPATH, '//input[contains(@class, "MuiAutocomplete-input") and @placeholder="Искать"]')
method_search = (By.XPATH, '//div[@role="combobox" and @class="MuiSelect-select MuiSelect-standard MuiSelect-multiple MuiInputBase-input MuiInput-input css-2z1u6n"]')
search_tag = (By.XPATH, '//span[text()="по тегам"]')
button_search = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/form/div/div[2]/div[1]/div/button')

class SearchProjectsSite(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(url='https://test.startupium.ru/projects')