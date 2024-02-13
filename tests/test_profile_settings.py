import time
import requests
from selenium.common.exceptions import NoSuchElementException
from page.profile_settings import ProfileSetting, position_form, warrning_position_form, warrning_position_form_leng


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
    '''Проверка уведомления меньше трех букв в поле должность при валидных данных'''
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    form.send_keys('AQA')
    try:
        message = profile_page.find(warrning_position_form_leng)
        assert message is None, 'Сообщение о содержание больше трех букв не появилось'
    except NoSuchElementException:
        f'Элемент не найден'
