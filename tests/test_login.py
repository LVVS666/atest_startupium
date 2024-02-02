import time

from page.login import Login, email_form, password_form, button_class, test_email, test_password, error_email



def test_login(browser):
    '''Проверка удачного логина при валидных данных'''
    login_page = Login(browser)
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
    time.sleep(5)
    current_url = login_page.browser.current_url
    assert current_url == 'https://startupium.ru/registration', 'Редирект не произошел'

def test_login_email_not_valid(browser):
    '''Проверка логина при невалидном email'''
    login_page = Login(browser)
    login_page.open()
    login_page.wait_element(email_form)
    email = login_page.find(email_form)
    email.send_keys('test@gmail.com')
    login_page.wait_element(password_form)
    password = login_page.find(password_form)
    password.send_keys(test_password)
    login_page.wait_element(button_class)
    button = login_page.find(button_class)
    button.click()
    login_page.wait_element(error_email)
    error_message = login_page.find(error_email)
    assert error_message is not None, 'Уведомления об ошибке не было'

def test_login_password_not_valid(browser):
    '''Проверка логина при невалидном пароле'''
    login_page = Login(browser)
    login_page.open()
    login_page.wait_element(email_form)
    email = login_page.find(email_form)
    email.send_keys(test_email)
    login_page.wait_element(password_form)
    password = login_page.find(password_form)
    password.send_keys('Test_password1!')
    login_page.wait_element(button_class)
    button = login_page.find(button_class)
    button.click()
    login_page.wait_element(error_email)
    error_message = login_page.find(error_email)
    assert error_message is not None, 'Уведомления об ошибке не было'