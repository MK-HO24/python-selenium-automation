from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_signin_page(context):
    context.app.target_signin_page.open_signin_page()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window()
    print(context.original_window)

@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
    context.app.target_signin_page.click_on_tc_link()




@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.target_signin_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.target_signin_page.verify_tc_open()


@then('User can close new window and switch back to original')
def back_to_original_window(context):
    context.app.target_signin_page.close()
    context.app.target_signin_page.switch_to_window_by_id(context.original_window)



