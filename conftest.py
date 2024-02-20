import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    driver = Chrome()
    yield driver
    driver.quit()

