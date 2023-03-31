from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage(Page):
    ATC_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')
    NO_COVERAGE_BTN = (By.CSS_SELECTOR, '#attachSiNoCoverage')
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[aria-label='New Arrivals']")
    WOMEN = (By.CSS_SELECTOR, "a[href*='fashion-womens']")


    def add_to_cart(self):
        self.find_element(*self.ATC_BUTTON).click()

    def no_coverage(self):
        try:
            self.find_element(*self.NO_COVERAGE_BTN).click()
        except:
            pass

    def hover_na(self):
        na_tab = self.find_element(*self.NEW_ARRIVALS)
        ActionChains(self.driver).move_to_element(na_tab).perform()

    def verify_deals(self):
        try:
            self.find_element(*self.WOMEN).click()
        except:
            raise Exception('Women deal group not detected')
