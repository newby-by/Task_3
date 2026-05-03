import json
import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import data
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from utils.methods.order import OrderMethod
from utils.methods.user import UserMethod


load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--br",
                     action="store",
                     default="chrome",
                     help=("The key to choose a browser: "
                           "chrome or firefox (default: chrome)"))


@pytest.fixture(scope='function')
def driver(pytestconfig):
    if pytestconfig.getoption("br") == "gecko":
        os.environ['GH_TOKEN'] = os.getenv('GH_TOKEN')
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
    token = UserMethod(UserMethod.REGISTER_URL).register(
        payload=user_with_all_data
    ).json().get('accessToken')

    yield user_with_all_data

    UserMethod(UserMethod.USER_URL).delete_user(
        headers={'Authorization': token}
    )


@pytest.fixture(scope='function')
def registered_user_with_2_orders(registered_user):
    response = UserMethod(UserMethod.LOGIN_URL).login(
        payload=data.UserData.data_for_login(registered_user)
    )
    token = response.json().get('accessToken')
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    OrderMethod(url=OrderMethod.ORDER_URL).order(
        payload=json.dumps(data.OrderData().buns_and_sauce),
        headers=headers
    )
    OrderMethod(url=OrderMethod.ORDER_URL).order(
        payload=json.dumps(data.OrderData().buns_only),
        headers=headers
    )

    return registered_user


@pytest.fixture(scope='function')
def user_with_order(registered_user):
    response = UserMethod(UserMethod.LOGIN_URL).login(
        payload=data.UserData.data_for_login(registered_user)
    )
    token = response.json().get('accessToken')
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = OrderMethod(url=OrderMethod.ORDER_URL).order(
        payload=json.dumps(data.OrderData().buns_and_sauce),
        headers=headers
    )

    return {
        'login_data': data.UserData.data_for_login(registered_user),
        'id_order': response.json().get('order').get('number')
    }


@pytest.fixture(scope='function')
def login_data_user_without_orders(registered_user):
    return data.UserData.data_for_login(registered_user)


@pytest.fixture(scope='function')
def login_data_user_with_2_orders(registered_user_with_2_orders):
    return data.UserData.data_for_login(registered_user_with_2_orders)


@pytest.fixture(scope='function')
def login_user(login_data_user_without_orders, driver):
    login_page = LoginPage(driver)
    login_page.open(url=data.LOGIN_URL)
    email = login_data_user_without_orders['email']
    password = login_data_user_without_orders['password']
    login_page.fill_up_login_form(email, password)

    return driver


@pytest.fixture(scope='function')
def login_user_with_order(user_with_order, driver):
    login_page = LoginPage(driver)
    login_page.open(url=data.LOGIN_URL)
    user_data = user_with_order['login_data']
    email = user_data['email']
    password = user_data['password']
    login_page.fill_up_login_form(email, password)

    return driver, user_with_order['id_order']


@pytest.fixture(scope='function')
def login_user_with_2_orders(login_data_user_with_2_orders, driver):
    login_page = LoginPage(driver)
    login_page.open(url=data.LOGIN_URL)
    email = login_data_user_with_2_orders['email']
    password = login_data_user_with_2_orders['password']
    login_page.fill_up_login_form(email, password)

    return driver
