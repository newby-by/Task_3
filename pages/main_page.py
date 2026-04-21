import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


@allure.title('The Page Object for main page app')
class MainPage(BasePage):
    ACCOUNT_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a")
    
    @allure.step('Move to Account page')
    def go_to_account(self):
        self.wait_element_clickable(MainPage.ACCOUNT_LINK)
        self.click(MainPage.ACCOUNT_LINK)
