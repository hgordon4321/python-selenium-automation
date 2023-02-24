from selenium.webdriver.common.by import By
from behave import given, when, then


ATC_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')


@when('Product is added to cart')
def prod_atc(context):
    context.driver.find_element(*ATC_BUTTON).click()
