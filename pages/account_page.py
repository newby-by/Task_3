import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import data
from pages.base_page import BasePage


@allure.title('The Page Object for main page app')
class AccountPage(BasePage):
    TITLE_PAGE = (By.XPATH, ".//main//p")
    TITLE = 'В этом разделе вы можете изменить свои персональные данные'
    ORDER_HISTORY_LINK = (By.XPATH, ".//a[text()='История заказов']")
    HISTORY = (
        By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList')]"
    )
    ORDER_CARDS = (
        By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList')]/li"
    )

    @allure.step('Move to Account page')
    def is_page_available(self):
        self.wait_element_clickable(AccountPage.TITLE_PAGE)
        return (
            self.get_url() == data.ACCOUNT_URL and
            self.driver.find_element(
                *AccountPage.TITLE_PAGE).text == AccountPage.TITLE
        )

    @allure.step('Open orders history')
    def open_orders_history(self):
        self.click(AccountPage.ORDER_HISTORY_LINK)

    @allure.step('History orders is available')
    def is_history_available(self):
        try:
            return bool(self.find_element(AccountPage.HISTORY))
        except TimeoutException:
            return False
