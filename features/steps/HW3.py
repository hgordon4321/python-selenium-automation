from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open(context):
    context.driver.get('https://www.amazon.com')


@when('Click on returns & orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify sign in page launches')
def check_signin(context):
    assert context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").is_displayed(), 'Sign in text not visible'


@when('Click cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart').click()


@then('Verify "Cart is empty" appears')
def check_cart(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty').is_displayed(), 'Cart is Empty not visible'