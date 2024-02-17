import time
import requests
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from page.profile_settings import ProfileSetting, position_form, warrning_position_form, warrning_position_form_leng, \
    profile_class, next_step_1, title_step_2


def test_warrning_form_positions(browser):
    '''Проверка уведомления об обязательно заполненном поле должность'''
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    form.click()
    profile_page.wait_element(warrning_position_form)
    assert profile_page.find(warrning_position_form), 'Сообщение об обязательном поле не появилось'


def test_warrning_form_positions_count_leng_1(browser):
    '''Проверка уведомления меньше трех букв в поле должность'''
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    form.send_keys('QA')
    profile_page.wait_element(warrning_position_form_leng)
    assert profile_page.find(warrning_position_form_leng), 'Сообщение о содержание больше трех букв не появилось '


def test_warrning_form_positions_count_leng_2(browser):
    '''Проверка уведомления меньше трех букв в поле должность'''
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    form.send_keys('QA')
    profile_page.wait_element(warrning_position_form_leng)
    assert profile_page.find(warrning_position_form_leng), 'Сообщение о содержание больше трех букв не появилось '


def test_validation_form_positions(browser):
    '''Проверка отсутствия уведомления меньше трех букв в поле должность при валидных данных'''
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    form.send_keys('AQA')
    try:
        message = profile_page.find(warrning_position_form_leng)
        assert message is None, 'Сообщение о содержание больше трех букв появилось'
    except NoSuchElementException:
        f'Элемент не найден'


def test_button_next_step_role_on(browser):
    '''Проверка активности кнопки перехода на следующий шаг при выбранной роли в проекте и валидных данных '''
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    form.send_keys('AQA')
    profile_page.wait_element(profile_class)
    profile_activate = profile_page.find(profile_class)
    profile_page.browser.execute_script('arguments[0].click()', profile_activate)
    button_step = profile_page.find(next_step_1)
    assert button_step.get_attribute('disabled') is None, 'Кнопка следующего шага активна при невыполнение условий'


def test_role_on(browser):
    '''Проверка перехода на следующий шаг при выбранной роли в проекте'''
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    form.send_keys('AQA')
    profile_page.wait_element(profile_class)
    profile_activate = profile_page.find(profile_class)
    profile_page.browser.execute_script('arguments[0].click()', profile_activate)
    profile_page.wait_element(next_step_1)
    button_step = profile_page.find(next_step_1)
    profile_page.browser.execute_script('arguments[0].click()', button_step)
    profile_page.wait_element(title_step_2)
    assert profile_page.find(title_step_2), 'Переход к следующему шагу не произошел'


def test_button_next_step_role_off(browser):
    '''Проверка активности кнопки перехода на следующий шаг при не выбранной роли в проекте '''
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    form.send_keys('AQA')
    profile_page.wait_element(next_step_1)
    button_step = profile_page.find(next_step_1)
    assert button_step.get_attribute('disabled'), 'Кнопка следующего шага активна при невыполнение условий'




