from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Help page for return')
def open_help(context):
    context.app.help_page.open_help_page()


@when('Select Help topic {option}')
def select_promo_and_coupons(context,option):
    context.app.help_page.select_topic(option)

# @then('Verify {option} page opened')
# def verify_return_open(context, option):
#     context.app.help_page.verify_header(option)

@then('Verify help {option} page opened')
def verify_header(context, option):
    context.app.help_page.verify_header(option)