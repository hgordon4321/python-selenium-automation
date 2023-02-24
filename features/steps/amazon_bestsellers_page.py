from selenium.webdriver.common.by import By
from behave import given, when, then


# Locators
BS_TABS = (By.CSS_SELECTOR, 'a[href*=bs_tab]')

# Is there a way to store the located elements as variables rather than locators with behave structure?
# I tried bt the context was an unresolved reference
# If possible is it a normal/acceptable practice?


@given('Navigate to bestsellers page')
def nav_bs (context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are 5 links in ribbon bar')
def check_bs_links(context):
    links = context.driver.find_elements(*BS_TABS)
    assert len(links) == 5, f'Expected 5 links, got {len(links)}'




