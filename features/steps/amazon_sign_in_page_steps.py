from behave import given, when, then


@then('Verify sign in page launches')
def check_signin(context):
    context.app.sign_in_page.check_sign_in_text()