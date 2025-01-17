from selenium.webdriver.common.by import By
from behave import given, when, then






@given('Open Amazon page')
def open_page(context):
    context.app.main_page.open_main()


@given('Navigate to product page: {url}')
def open_prod(context, url):
    context.driver.get(url)


@when('Main page product link is clicked')
def open_product(context):
    context.app.main_page.click_prod_group()


@when('Click on returns & orders')
def click_orders(context):
    context.app.main_page.orders_click()


@when('Click cart icon')
def click_cart(context):
    context.app.main_page.cart_click()


@when('Filter search to {category}')
def filter_search(context, category):
    context.app.main_page.filter_search(category)


@when('Enter {item} in search box')
def enter_search_text(context, item):
    context.app.main_page.enter_search_text(item)




