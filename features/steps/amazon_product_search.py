from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT = (By.CSS_SELECTOR, "figure[data-test='product']")


@when('First product is selected')
def sel_prod(context):
    context.driver.find_element(*PRODUCT).click()
# I assumed it was ok to click the product/picture instead of the price as the products
# were generated from the picture click instead of a search
