import pytest

from selenium.webdriver import Chrome


@pytest.fixture()
def browser():
    driver = Chrome()
    yield driver
    driver.quit()