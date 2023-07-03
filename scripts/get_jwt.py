import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.duolingo.com")

username = ...
password = ...

login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/header/div[2]/div[2]/div/button')
login_button.click()

email_field = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/form/div[1]/div[1]/div[1]/input')
email_field.send_keys(username)

password_field = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/form/div[1]/div[1]/div[2]/input')
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

print(driver.execute_script("document.cookie.match(new RegExp('(^| )jwt_token=([^;]+)'))[0].slice(11);"))

# does not work