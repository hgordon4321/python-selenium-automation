from pages.base_page import Page
from selenium.webdriver.common.by import By
import time

class CartPage(Page):
    CART_EMPTY = (By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty')
    CART_COUNT = (By.CSS_SELECTOR, '#nav-cart-count')

    def cart_count_check(self):
        time.sleep(1)
        cart_count = self.find_element(*self.CART_COUNT).text
        assert cart_count == '1', f'Expected 1 item, got {cart_count}'

    def cart_check(self):
        assert self.find_element(*self.CART_EMPTY).is_displayed(), 'Cart is Empty not visible'