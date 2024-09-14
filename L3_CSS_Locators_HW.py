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

driver.get('https://www.amazon.com/')
sleep(8)

driver.find_element(By.CSS_SELECTOR,'#nav-link-accountList-nav-line-1').click()
sleep(4)
driver.find_element(By.CSS_SELECTOR,"#createAccountSubmit").click()
sleep(4)
driver.find_element(By.CSS_SELECTOR,".a-icon.a-icon-logo[aria-label='Amazon']")
driver.find_element(By.CSS_SELECTOR,"div.a-box-inner .a-spacing-small")
driver.find_element(By.CSS_SELECTOR,"[name='customerName']")
driver.find_element(By.CSS_SELECTOR,"[name='email']")
driver.find_element(By.CSS_SELECTOR,"#ap_password[type='password']")
driver.find_element(By.CSS_SELECTOR,"[name='passwordCheck'][type='password']")
driver.find_element(By.CSS_SELECTOR,"#continue[type='submit']")
driver.find_element(By.XPATH,"//div[@id='legalTextRow']//a[text()='Conditions of Use']")
driver.find_element(By.XPATH,"//div[@id='legalTextRow']//a[text()='Privacy Notice']")
driver.find_element(By.XPATH,"//div[@class='a-row']//a[@class='a-link-emphasis']")
