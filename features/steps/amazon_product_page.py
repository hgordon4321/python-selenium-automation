from selenium.webdriver.common.by import By
from behave import given, when, then



PROD_COLORS = (By.CSS_SELECTOR, 'li[id*=color_name]')
COLOR_FIELD = (By.CSS_SELECTOR, 'span.selection')


@when('Product is added to cart')
def prod_atc(context):
    context.app.prod_page.add_to_cart()
    context.app.prod_page.no_coverage()


@then('Verify color is correct for first 5 products')
def color_check(context):
    colors = context.driver.find_elements(*PROD_COLORS)
    eColors = ['Black', 'Clove Purple', 'Deep Red', 'Fluorescent Green', 'Kumquat']

    for i in range(5):
        colors[i].click()
        assert context.driver.find_element(*COLOR_FIELD).text == eColors[i], f'Expected color field to read {eColors[i]}, actually read {context.driver.find_element(*COLOR_FIELD).text}'
