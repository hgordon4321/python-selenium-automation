from selenium.webdriver.common.by import By
from behave import given, when, then





@then('Verify cart has 1 item')
def cart_count_check(context):
    context.app.cart_page.cart_count_check()


@then('Verify "Cart is empty" appears')
def check_cart(context):
    context.app.cart_page.cart_check()