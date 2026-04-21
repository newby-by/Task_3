import allure
from selenium.webdriver.common.by import By

import data
from pages.base_page import BasePage


@allure.title('The Page Object for main page app')
class MainPage(BasePage):
    TITLE_PAGE = (By.XPATH, ".//h1")
    TITLE = 'Соберите бургер'
    
    @allure.step('Check main page is available')
    def is_page_available(self):
        self.wait_element_clickable(MainPage.TITLE_PAGE)
        return (
            self.get_url() == data.CONSTRUCTOR_URL and
            self.find_element(MainPage.TITLE_PAGE).text ==
            MainPage.TITLE
        )
