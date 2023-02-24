from selenium.webdriver.common.by import By
from behave import given, when, then


CART_COUNT = (By.CSS_SELECTOR, '#nav-cart-count')


@then('Verify cart has 1 item')
def cart_count_check(context):
    cart_count = context.driver.find_element(*CART_COUNT).text
    assert cart_count == '1', f'Expected 1 item, got {cart_count}'

