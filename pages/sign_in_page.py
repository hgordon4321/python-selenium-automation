from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

    def check_sign_in_text(self):
        assert self.find_element(*self.SIGN_IN_TEXT).is_displayed(), 'Sign in text not visible'

# When I break the locator I am getting a no such element exception instead of an assertion error
# Is there a problem with the assertion? To make it an assertion error would I need to use a try block?