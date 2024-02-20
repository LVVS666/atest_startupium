from .base_page import BasePage
from page.login import test_email, test_password, Login, email_form, password_form, button_class
from selenium.webdriver.common.by import By


position_form = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/div/div[1]/div[2]/ul/li[2]/div/div/input')
warrning_position_form = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/div/div[1]/div[2]/ul/li[2]/div/p')
warrning_position_form_leng = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/div/div[1]/div[2]/ul/li[2]/div/p')
profile_class = (By.CLASS_NAME, 'css-1qh42pp')
title_step_2 = (By.CLASS_NAME, 'css-ecaa79')
next_step_1 = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/div[2]/button')
form_tag = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/input')
added_tag = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/span')
delete_tag = (By.CSS_SELECTOR, '#__next > div.css-1c4mae2 > main > div > div > div:nth-child(2) > div.css-0 > div > div > div.MuiBox-root.css-1atepvb > div.MuiBox-root.css-0 > div > div > svg > path')
button_next = (By.XPATH, '//*[@id="__next"]/div[2]/main/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/span[1]/span[1]/input')
form_name_company = (By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/form/div/div[1]/div[2]/div/input')



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
