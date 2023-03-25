from selenium.webdriver.common.by import By
from behave import given, when, then



@when('First product is selected')
def sel_prod(context):
    context.app.prod_group_page.product_click()

