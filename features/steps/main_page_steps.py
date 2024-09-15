from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify header has {expected_amount} links')
def link_count(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR,"[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print(links)
    assert len(links) == int(expected_amount),f"Expected {expected_amount} links, got {len(links)}"


@then ('Verify header is shown')
def link_shown(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='l-container-fixed styles_utilityHeaderContainer']")

@then ('Verify header has links')
def verify_links_shown(context):
    links = context.driver.find_elements (By.CSS_SELECTOR,"[data-test*='@web/GlobalHeader/UtilityHeader/']")
    assert len(links) > 0, "No links found"