
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click Sign in Right Nav Menu')
def click_sign_in_right(context):
    # context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']").click()
    context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']"))).click()

@then ('Verify Sign In form opened')
def verify_sign_in_form(context):
    actual_text = context.driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
    expected_text = 'Sign into your Target account'
    assert expected_text in actual_text, f'Expected {expected_text}, got actual {actual_text}'