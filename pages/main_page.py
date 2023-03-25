from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    ORDERS = (By.ID, 'nav-orders')
    CART = (By.CSS_SELECTOR, '#nav-cart')
    HANDBAGS = (By.CSS_SELECTOR, "img[alt='Handbags']")

    def open_main(self):
        self.open_url('https://www.amazon.com/')

    def orders_click(self):
        self.find_element(*self.ORDERS).click()

    def cart_click(self):
        self.find_element(*self.CART).click()

    def click_prod_group(self):
        self.find_element(*self.HANDBAGS).click()
