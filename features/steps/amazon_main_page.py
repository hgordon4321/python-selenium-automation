import random
from selenium.webdriver.common.by import By
from behave import given, when, then


MAIN_PIC = (By.CSS_SELECTOR, 'div.fluid-image-container')


@given('Open Amazon page')
def open_page(context):
    context.driver.get('https://www.amazon.com')


@when('Main page product link is clicked')
def open_product(context):
    pics = context.driver.find_elements(*MAIN_PIC)
    pic_count = len(pics)
    print(pic_count)
    random.choice(pics).click()








