import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


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
