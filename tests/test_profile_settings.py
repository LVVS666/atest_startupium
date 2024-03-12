import time

import allure
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from page.profile_settings import ProfileSetting, position_form, warrning_position_form, warrning_position_form_leng, \
    profile_class, next_step_1, title_step_2, form_tag, added_tag, delete_tag, button_next, form_name_company, add_work, \
    button_next_3, form_specialist, form_charge, month_start, year_start, checkbox_today, comany_add


@allure.feature('Первый шаг редактирования профиля')
@allure.story('Валидация поля должность')
@allure.title('Уведомления об обязательно заполненном поле должность')
def test_warrning_form_positions(browser):
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    with allure.step('Поле должность незаполненно.'):
        form.click()
    with allure.step('Проверка сообщения об незаполненном поле'):
        profile_page.wait_element(warrning_position_form)
        assert profile_page.find(warrning_position_form), 'Сообщение об обязательном поле не появилось'


@allure.feature('Первый шаг редактирования профиля')
@allure.story('Валидация поля должность')
@allure.title('Уведомление меньше трех букв в поле должность при двух буквах в форме')
def test_warrning_form_positions_count_leng_1(browser):
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    with allure.step('Заполнена одна буква в поле "Должность"'):
        form.send_keys('Q')
    with allure.step('Проверка сообщения "Количество символов в должности не мньше трех"'):
        profile_page.wait_element(warrning_position_form_leng)
        assert profile_page.find(warrning_position_form_leng), 'Сообщение о содержание больше трех букв не появилось '


@allure.feature('Первый шаг редактирования профиля')
@allure.story('Валидация поля должность')
@allure.title('Уведомление меньше трех букв в поле должность при одной букве в форме')
def test_warrning_form_positions_count_leng_2(browser):
    '''Проверка уведомления меньше трех букв в поле должность'''
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    with allure.step('Заполнены две буквы в поле "Должность"'):
        form.send_keys('QA')
    with allure.step('Проверка сообщения "Количество символов в должности не мньше трех" '):
        profile_page.wait_element(warrning_position_form_leng)
        assert profile_page.find(warrning_position_form_leng), 'Сообщение о содержание больше трех букв не появилось '



@allure.feature('Первый шаг редактирования профиля')
@allure.story('Валидация поля должность')
@allure.title('Отсутствие уведомления меньше трех букв в поле должность при валидных данных')
def test_validation_form_positions(browser):
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    with allure.step('Заполнены валидные данные в поле "Должность"'):
        form.send_keys('AQA')
    try:
        with allure.step('Сообщение о "Содержание больше трех букв" не появилось'):
            message = profile_page.find(warrning_position_form_leng)
            assert message is None, 'Сообщение о содержание больше трех букв появилось'
    except NoSuchElementException:
        f'Элемент не найден'



@allure.feature('Первый шаг редактирования профиля')
@allure.title('Активность кнопки перехода на следующий шаг, при выбранной роли в проекте и валидных данных')
def test_button_next_step_role_on(browser):
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    with allure.step('Заполнены валидные данные в поле "Должность"'):
        form.send_keys('AQA')
    profile_page.wait_element(profile_class)
    profile_activate = profile_page.find(profile_class)
    with allure.step('Выбрана роль в проекте'):
        profile_page.browser.execute_script('arguments[0].click()', profile_activate)
    button_step = profile_page.find(next_step_1)
    with allure.step('Кнопка для перехода на следующий шаг активна'):
        assert button_step.get_attribute('disabled') is None, 'Кнопка следующего шага неактивна при выполненых условях'


@allure.feature('Первый шаг редактирования профиля')
@allure.title('Активность кнопки перехода на следующий шаг при не выбранной роли в проекте и валидных данных')
def test_button_next_step_role_off(browser):
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    with allure.step('Заполнены валидные данные в поле "Должность"'):
        form.send_keys('AQA')
    with allure.step('Роль на проекте не выбрана'):
        profile_page.wait_element(next_step_1)
    button_step = profile_page.find(next_step_1)
    with allure.step('Кнопка для перехода на следующий шаг неактивна'):
        assert button_step.get_attribute('disabled'), 'Кнопка следующего шага активна при невыполнение условий'


@allure.feature('Первый шаг редактирования профиля')
@allure.title('Переход на следующий шаг, при валидных данных и выбранной роли в проекте')
def test_role_on(browser):
    profile_page = ProfileSetting(browser)
    profile_page.open()
    profile_page.wait_element(position_form)
    form = profile_page.find(position_form)
    with allure.step('Заполнены валидные данные в поле "Должность"'):
        form.send_keys('AQA')
    profile_page.wait_element(profile_class)
    profile_activate = profile_page.find(profile_class)
    with allure.step('Выбрана роль в проекте'):
        profile_page.browser.execute_script('arguments[0].click()', profile_activate)
    profile_page.wait_element(next_step_1)
    button_step = profile_page.find(next_step_1)
    with allure.step('Переход на следующий шаг'):
        profile_page.browser.execute_script('arguments[0].click()', button_step)
    profile_page.wait_element(title_step_2)
    assert profile_page.find(title_step_2), 'Переход к следующему шагу не произошел'


@allure.feature('Второй шаг редактирования профиля')
@allure.story('Добавление навыков')
@allure.title('Проверка возможности добавить новый навык и его успешное добавление')
def test_add_tag(browser):
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
    profile_page.wait_element(form_tag)
    tag_add = profile_page.find(form_tag)
    with allure.step('Добавить новый навык'):
        tag_add.send_keys('Profession')
    tag_add.send_keys(Keys.ENTER)
    profile_page.wait_element(added_tag)
    tag = profile_page.find(added_tag)
    with allure.step('Навык отобразился в добавленных'):
        assert tag.text == 'Profession', 'Создался неверный навык'


@allure.feature('Второй шаг редактирования профиля')
@allure.story('Добавление навыков')
@allure.title('Проверка возможности удаление навыка.')
def test_delete_tag(browser):
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
    profile_page.wait_element(form_tag)
    tag_add = profile_page.find(form_tag)
    with allure.step('Добавить новый навык'):
        tag_add.send_keys('Profession')
    tag_add.send_keys(Keys.ENTER)
    with allure.step('Удалить новый навык'):
        profile_page.wait_element(delete_tag)
    profile_page.find(delete_tag).click()
    try:
        assert profile_page.find(added_tag) is None, 'Элемент не удалился'
    except NoSuchElementException:
        f'Элемент успешно удален'

@allure.feature('Второй шаг редактирования профиля')
@allure.story('Добавление навыков')
@allure.title('Проверка возможности удаление навыка кнопкой DELETE')
def test_delete_tag_delete(browser):
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
    profile_page.wait_element(form_tag)
    tag_add = profile_page.find(form_tag)
    with allure.step('Добавить новый навык'):
        tag_add.send_keys('Profession')
    tag_add.send_keys(Keys.ENTER)
    tag_add = profile_page.find(form_tag)
    with allure.step('Удалить навык кнопкой DELETE'):
        tag_add.send_keys(Keys.DELETE)
        tag_add.send_keys(Keys.DELETE)
    try:
        assert profile_page.find(added_tag), 'Элемент удалился'
    except NoSuchElementException:
        f'Элемент успешно удален'


@allure.feature('Второй шаг редактирования профиля')
@allure.title('Проверка использования кнопки "Заполню потом" и активности кнопки следующий шаг')
def test_next_button_actived(browser):
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
    profile_page.wait_element(button_next)
    with allure.step('Активировать кнопку "Заполню потом"'):
        profile_page.find(button_next).click()
    button_step = profile_page.find(next_step_1)
    assert button_step.get_attribute('disabled') is None, 'Кнопка следующего шага неактивна при выполнение условий'


@allure.feature('Второй шаг редактирования профиля')
@allure.title('Проверка активности кнопки "Следующий шаг" при незаполненных условиях')
def test_next_button_disabled(browser):
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
    button_step = profile_page.find(next_step_1)
    with allure.step('Условия невыполнены - кнопка перехода на следующий шаг не активна'):
        assert button_step.get_attribute('disabled'), 'Кнопка следующего шага активна при выполнение условий'


@allure.feature('Второй шаг редактирования профиля')
@allure.title('Проверка перехода к следующему шагу "Ваша Карьера"')
def test_next_step(browser):
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
    profile_page.wait_element(form_tag)
    tag_add = profile_page.find(form_tag)
    with allure.step('Добавить новый навык'):
        tag_add.send_keys('Profession')
    tag_add.send_keys(Keys.ENTER)
    button_step = profile_page.find(next_step_1)
    profile_page.browser.execute_script('arguments[0].click()', button_step)
    profile_page.wait_element(form_name_company)
    with allure.step('Условия выполнены - происходит переход к следующему шагу'):
        assert profile_page.find(form_name_company), 'Переход к следующему шагу,с соблюдением условий,не произошел'


@allure.feature('Третий шаг редактирования профиля')
@allure.title('Проверка активности добавления работы при незаполненных данных')
def test_action_button_added_work(browser):
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
    profile_page.wait_element(button_next)
    profile_page.find(button_next).click()
    profile_page.find(next_step_1).click()
    profile_page.wait_element(add_work)
    button_add_work = profile_page.find(add_work)
    with allure.step('Данные незаполнены - кнопка неактивна.'):
        assert button_add_work.get_attribute('disabled'), 'Кнопка активна при не заполненных полях'


@allure.feature('Третий шаг редактирования профиля')
@allure.title('Проверка добавления работы при валидных данных')
def test_added_work(browser):
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
    profile_page.wait_element(button_next)
    profile_page.find(button_next).click()
    profile_page.find(next_step_1).click()
    profile_page.wait_element(form_name_company)
    company = profile_page.find(form_name_company)
    with allure.step('Заполнено название компании'):
        company.send_keys('Ozon')
    profile_page.wait_element(form_specialist)
    specialist = profile_page.find(form_specialist)
    with allure.step('Заполнена должность в компании'):
        specialist.send_keys('QA')
    profile_page.wait_element(form_charge)
    charge = profile_page.find(form_charge)
    with allure.step('Заполнены обязанности в компании'):
        charge.send_keys('Testing site and products')
    profile_page.wait_element(month_start)
    month = profile_page.find(month_start)
    with allure.step('Заполнен месяц начала'):
        month.send_keys('Январь')
    month.send_keys(Keys.ENTER)
    profile_page.wait_element(year_start)
    year = profile_page.find(year_start)
    with allure.step('Заполнен год начала'):
        year.send_keys('2020')
    with allure.step('Дата окончания - По настоящее время'):
        profile_page.wait_element(checkbox_today)
    today = profile_page.find(checkbox_today)
    profile_page.browser.execute_script('arguments[0].click()', today)
    profile_page.wait_element(add_work)
    add = profile_page.find(add_work)
    with allure.step('Добавления места работы'):
        profile_page.browser.execute_script('arguments[0].click()', add)
    profile_page.wait_element(comany_add)
    assert profile_page.find(comany_add), 'Место работы не добавилось'



@allure.feature('Третий шаг редактирования профиля')
@allure.title('Проверка активности кнопки "Следующий шаг" при незаполненных данных и без активной кнопки "заполню потом"')
def test_action_button_next_step_not_active(browser):
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
    profile_page.wait_element(button_next)
    profile_page.find(button_next).click()
    profile_page.find(next_step_1).click()
    profile_page.wait_element(next_step_1)
    next_button = profile_page.find(next_step_1)
    with allure.step('Данные незаполненны - кнопка неактивна'):
        assert next_button.get_attribute('disabled'), 'Кнопка активна при незаполненных данных'


@allure.feature('Третий шаг редактирования профиля')
@allure.title('Проверка активности кнопки "Следующий шаг" при незаполненных данных,но с активацией кнопки "заполню потом"')
def test_action_button_next_step_active(browser):
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
    profile_page.wait_element(button_next)
    profile_page.find(button_next).click()
    profile_page.find(next_step_1).click()
    profile_page.wait_element(button_next_3)
    button_step_2 = profile_page.find(button_next_3)
    with allure.step('Активация кнопки "Заполню потом"'):
        profile_page.browser.execute_script('arguments[0].click()', button_step_2)
    profile_page.wait_element(next_step_1)
    next_button = profile_page.find(next_step_1)
    with allure.step('Кнопка перехода на следующий шаг активна'):
        assert next_button.get_attribute('disabled') is None, 'Кнопка не активна при незаполненных данных'
