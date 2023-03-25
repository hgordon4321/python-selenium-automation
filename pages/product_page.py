from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProductPage(Page):
    ATC_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')
    NO_COVERAGE_BTN = (By.CSS_SELECTOR, '#attachSiNoCoverage')

    def add_to_cart(self):
        self.find_element(*self.ATC_BUTTON).click()

    def no_coverage(self):
        try:
            self.find_element(*self.NO_COVERAGE_BTN).click()
        except:
            pass
