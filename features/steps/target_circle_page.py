from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')
    sleep(4)


@then('Verify page has 10 benefit cells')
def verify_benefit_cells(context):
    links = context.driver.find_elements(By.CSS_SELECTOR,"p[class='h-text-md']")
    assert len(links) == 10, f"Expected 10 benefit cells, got {len(links)}"