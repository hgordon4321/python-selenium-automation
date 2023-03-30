from selenium.webdriver.common.by import By
from behave import given, when, then


@when('First product is selected')
def sel_prod(context):
    context.app.prod_group_page.product_click()


@then('Store name of product number {num}')
def store_prod(context, num):
    try:
        context.prods.append(context.app.prod_search.get_prod_name(int(num)))
    except AttributeError:
        context.prods = []
        context.prods.append(context.app.prod_search.get_prod_name(int(num)))
    print(context.prods)

@then('Verify product names are different')
def prod_name_check(context):
    assert context.prods[0] != context.prods[1], 'Same product found in both categories'
