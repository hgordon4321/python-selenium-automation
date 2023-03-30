from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class MainPage(Page):
    ORDERS = (By.ID, 'nav-orders')
    CART = (By.CSS_SELECTOR, '#nav-cart')
    HANDBAGS = (By.CSS_SELECTOR, "img[alt='Handbags']")
    SEARCH_FILTER = (By.CSS_SELECTOR, '#searchDropdownBox')
    SEARCH_BOX = (By.CSS_SELECTOR, '#twotabsearchtextbox')


    def open_main(self):
        self.open_url('https://www.amazon.com/')

    def orders_click(self):
        self.find_element(*self.ORDERS).click()

    def cart_click(self):
        self.find_element(*self.CART).click()

    def click_prod_group(self):
        self.find_element(*self.HANDBAGS).click()

    def filter_search(self, category):
        dropdown = Select(self.find_element(*self.SEARCH_FILTER))
        dropdown.select_by_visible_text(category)

    def enter_search_text(self, text):
        self.input_text(text, *self.SEARCH_BOX)



