import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import data
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


def pytest_addoption(parser):
    parser.addoption("--br",
                     action="store",
                     default="chrome",
                     help=("The key to choose a browser: "
                           "chrome or firefox (default: chrome)"))


@pytest.fixture(scope='function')
def driver(pytestconfig):
    if pytestconfig.getoption("br") == "gecko":
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install()
        )
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def reset_password_page(driver):
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.open(data.FORGOT_PASSWORD_URL)
    forgot_password_page.fill_email_up(data.UserData().email)
    forgot_password_page.restore_password()

    return ResetPasswordPage(forgot_password_page.driver)
