import allure
from selenium.webdriver.common.by import By

import data
from pages.base_page import BasePage


@allure.title('The Page Object for main page app')
class AccountPage(BasePage):
    TITLE_PAGE = (By.XPATH, ".//main//p")
    TITLE = 'В этом разделе вы можете изменить свои персональные данные'
    
    @allure.step('Move to Account page')
    def is_page_available(self):
        self.wait_element_clickable(AccountPage.TITLE_PAGE)
        return (
            self.get_url() == data.ACCOUNT_URL and
            self.driver.find_element(
                *AccountPage.TITLE_PAGE).text == AccountPage.TITLE
        )
