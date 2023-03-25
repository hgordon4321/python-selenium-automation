from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProductGroupPage(Page):
    PRODUCT = (By.CSS_SELECTOR, 'div.s-image-tall-aspect')

    def product_click(self):
        self.find_element(*self.PRODUCT).click()