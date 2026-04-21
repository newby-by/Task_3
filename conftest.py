import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import data
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from utils.methods.user import UserMethod


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


@pytest.fixture(scope='function')
def user():
    return data.UserData()


@pytest.fixture(scope='function')
def user_with_all_data(user):
    return user.with_all_data


@pytest.fixture(scope='function')
def registered_user(user_with_all_data):
    UserMethod(UserMethod.REGISTER_URL).register(
            payload=user_with_all_data
    )
    return user_with_all_data


@pytest.fixture(scope='function')
def login_data(registered_user):
    return data.UserData.data_for_login(registered_user)


@pytest.fixture(scope='function')
def login(login_data, driver):
    login_page = LoginPage(driver)
    login_page.open(url=data.LOGIN_URL)
    email, password = login_data['email'], login_data['password']
    login_page.fill_up_login_form(email, password)

    return driver
