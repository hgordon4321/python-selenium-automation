from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProductSearchPage(Page):
    PRODUCT_TITLES = (By.CSS_SELECTOR, 'span.a-size-base-plus')

    def get_prod_name(self, prod_num):
        return self.find_elements(*self.PRODUCT_TITLES)[prod_num-1].text
