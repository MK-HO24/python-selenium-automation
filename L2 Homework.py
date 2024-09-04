from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Homework part 1



driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

sleep(10)

driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")
driver.find_element(By.ID,"ap_email")
driver.find_element(By.ID,"continue")
driver.find_element(By.XPATH,"//div[@id='legalTextRow']//a[text()='Conditions of Use']")
driver.find_element(By.XPATH,"//div[@id='legalTextRow']//a[text()='Privacy Notice']")
driver.find_element(By.ID, 'ab-signin-ingress-link')
driver.find_element(By.ID, 'createAccountSubmit')
sleep(3)

driver.quit()



# Homework part 2

driver.get('https://www.target.com/')

driver.find_element(By.XPATH,"//a[@data-test = '@web/AccountLink']//span[text()='Sign in']").click()
driver.find_element(By.XPATH,"//a[@data-test = 'accountNav-signIn']").click()

sleep(5)

actual_text = driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
expected_text = 'Sign into your Target account'

sleep(5)

assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
print(f"Expected text '{expected_text}' was found, Test Case passed")

sleep(3)

driver.find_element(By.ID,"login").click()

sleep(2)

driver.quit()

#Optional challenge:

driver.get("https://www.target.com/")

driver.find_element(By.ID,"search").send_keys("apples")
driver.find_element(By.XPATH,"//*[@data-test='@web/Search/SearchButton']").click()

sleep(4)

actual_word = driver.find_element(By.XPATH,"//div[@data-test='resultsHeading']").text
expected_word = "apples"



assert expected_word in actual_word, f"Expected '{expected_word}', but got '{actual_word}'"
print(f"Expected result '{expected_word}' found")

sleep(3)

driver.quit()