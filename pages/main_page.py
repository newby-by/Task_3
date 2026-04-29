import random

import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import pages


@allure.title('The Page Object for main page app')
class MainPage(pages.BasePage):
    TITLE_PAGE = (By.XPATH, ".//h1")
    TITLE = 'Соберите бургер'
    INGREDIENTS_CARDS_SELECTOR = ".//main//ul//a"
    NUMBER_INGREDIENTS_CARDS = lambda number: (
        By.XPATH, f"(.//main//ul//a)[{number}]"
    )
    INGREDIENTS_CARDS_ATTRIBUTE = lambda number, selector: (
        By.XPATH, f"(.//main//ul//a)[{number}]{selector}"
    )
    COUNTER_INGREDIENT_SELECTOR = "//p[contains(@class, 'counter')]"
    PRICE_INGREDIENT_SELECTOR = "//p[contains(@class, 'ingredient__price')]"
    NAME_INGREDIENT_SELECTOR = "//p[contains(@class, 'ingredient__text')]"
    INGREDIENT_MODAL_WINDOW = lambda selector: (
        By.XPATH, f".//section[contains(@class, 'modal_opened')]{selector}"
    )
    TITLE_MODAL_WINDOW_SELECTOR = "//h2"
    TITLE_MODAL_WINDOW = "Детали ингредиента"
    NAME_INGREDIENT_IN_MODAL_WINDOW_SELECTOR = "//p"
    CLOSE_CARD_BUTTON = (
        By.XPATH,
        (".//h2[text()='Детали ингредиента']/"
         "parent::div/following-sibling::button")
    )
    CONSTRUCTOR = (By.XPATH, ".//ul[contains(@class,'BurgerConstructor')]")
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    TITLE_ORDER = "идентификатор заказа"
    IDENTIFIER_ORDER = 1
    ORDER_MODAL_WINDOW = lambda number: (
        By.XPATH,
        f"(.//section[contains(@class, 'Modal_modal_opened')]//p)[{number}]"
    )
    NUMBER_ORDER_MODAL_WINDOW = (
        By.XPATH,
        ".//section[contains(@class, 'Modal_modal_opened')]//h2"
    )
    ORDER_BUTTON_WINDOW = (
        By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button"
    )

    @allure.step('Check main page is available')
    def is_page_available(self):
        self.wait_element_located(MainPage.TITLE_PAGE)
        return (
            self.get_url() == data.CONSTRUCTOR_URL and
            self.find_element(MainPage.TITLE_PAGE).text ==
            MainPage.TITLE
        )

    @allure.step('Open ingredient card with number is {number}')
    def open_ingredient_card_with(self, number):
        self.click(MainPage.NUMBER_INGREDIENTS_CARDS(number))

    @allure.step('Close ingredient card')
    def close_ingredient_card(self):
        self.click(MainPage.CLOSE_CARD_BUTTON)


    @allure.step('Get ingredient data from constructor page')
    def get_ingredient_data_from_constructor(self, number):
        counter = self.find_element(
            MainPage.INGREDIENTS_CARDS_ATTRIBUTE(
                number,
                MainPage.COUNTER_INGREDIENT_SELECTOR
            )
        ).text
        price = self.find_element(
            MainPage.INGREDIENTS_CARDS_ATTRIBUTE(
                number,
                MainPage.PRICE_INGREDIENT_SELECTOR
            )
        ).text
        name = self.find_element(
            MainPage.INGREDIENTS_CARDS_ATTRIBUTE(
                number,
                MainPage.NAME_INGREDIENT_SELECTOR
            )
        ).text
        
        return {
            'counter': counter,
            'price': price,
            'name': name
        }
    
    @allure.step('Get title ingredient modal window')
    def get_title_ingredient_modal_window(self):
        return self.find_element(
            MainPage.INGREDIENT_MODAL_WINDOW(
                MainPage.TITLE_MODAL_WINDOW_SELECTOR
            )
        ).text
       
    @allure.step('Get name ingredient modal window')
    def get_name_ingredient_modal_window(self):
        return self.find_element(
            MainPage.INGREDIENT_MODAL_WINDOW(
                MainPage.NAME_INGREDIENT_IN_MODAL_WINDOW_SELECTOR
            )
        ).text
    
    @property
    def number_of_cards(self):
        return len(self.find_elements(
            (By.XPATH, MainPage.INGREDIENTS_CARDS_SELECTOR)
        ))

    @allure.step('Drag and drop card {number} to constructor')
    def drag_and_drop_card_to_constructor_with(self, number):
        source_element = self.find_element(
            MainPage.NUMBER_INGREDIENTS_CARDS(number)
        )
        target_element = self.find_element(MainPage.CONSTRUCTOR)

        ActionChains(self.driver).drag_and_drop(
            source_element, target_element
        ).perform()

    def make_burger(self):
        random_bun = random.randint(1, 2)
        self.drag_and_drop_card_to_constructor_with(random_bun)
        random_sauce = random.randint(3, 6)
        self.drag_and_drop_card_to_constructor_with(random_sauce)
        random_main = random.randint(7, self.number_of_cards)
        self.drag_and_drop_card_to_constructor_with(random_main)

    def is_order_window_available(self):
        order_number = self.get_order_number_in_window()
        return (
            self.find_element(
                MainPage.ORDER_MODAL_WINDOW(MainPage.IDENTIFIER_ORDER)
            ).text == MainPage.TITLE_ORDER and
            order_number != '9999'
        )
    
    def get_order_number_in_window(self):
        self.wait_text_in_element_disappeared(
            MainPage.NUMBER_ORDER_MODAL_WINDOW,
            '9999',
            timeout=20
        )
        return self.find_element(MainPage.NUMBER_ORDER_MODAL_WINDOW).text

    @allure.step('Click on order button')    
    def click_on_order_button(self):
        self.click(MainPage.ORDER_BUTTON)

    @allure.step('Close the order window')    
    def close_window(self):
        self.wait_visibility_of_element_located(
            MainPage.ORDER_BUTTON_WINDOW
        )
        self.wait_element_located(
            MainPage.ORDER_BUTTON_WINDOW
        )
        self.click(MainPage.ORDER_BUTTON_WINDOW)
