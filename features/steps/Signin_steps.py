
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click Sign in Right Nav Menu')
def click_sign_in_right(context):
    context.app.signin_page.click_sign_in_right()

    # context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']").click()
    # context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']"))).click()

@when('Input user name')
def input_user_name(context):
    context.app.signin_page.input_user_name()

@when('Input incorrect user name')
def input_user_name(context):
    context.app.signin_page.input_wrong_user_name()

@when('Input password')
def input_password(context):
    context.app.signin_page.input_password()

@when('Input incorrect password')
def input_password(context):
    context.app.signin_page.input_wrong_password()

@when ('Click signin button')
def click_signin_button(context):
    context.app.signin_page.click_signin_button()

@then ('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.signin_page.verify_sign_in_form()

    # actual_text = context.driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
    # expected_text = 'Sign into your Target account'
    # assert expected_text in actual_text, f'Expected {expected_text}, got actual {actual_text}'

@then ('Verify user is logged in')
def verify_user_is_logged_in(context):
    context.app.signin_page.verify_user_is_logged_in()


@then ('Verify error messge is displayed')
def verify_error_message(context):
    context.app.signin_page.verify_error_message()