from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


PRIV_POL = (By.CSS_SELECTOR, 'div.help-content a[href*=privacy]')
PRIV_HEADER = (By.CSS_SELECTOR, 'div.help-service-content h1')


@given('Open Amazon T&C page')
def open_tc(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Click on Amazon Privacy Notice link')
def priv_click(context):
    context.driver.find_element(*PRIV_POL).click()


@when('Switch to the newly opened window')
def win_switch(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.win_handles = context.driver.window_handles
    context.driver.switch_to.window(context.win_handles[1])


@then('Verify Amazon Privacy Notice page is opened')
def priv_check(context):
    assert context.driver.find_element(*PRIV_HEADER).text == 'Amazon.com Privacy Notice',\
        'Page header read incorrectly'


@then('User can close new window and switch back to original')
def win_close(context):
    context.driver.close()
    context.driver.switch_to.window(context.win_handles[0])


