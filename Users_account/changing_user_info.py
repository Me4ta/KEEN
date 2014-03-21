##test scenario
# Given I changed in account fields with first and last name
# When I click the "Save" button
# Then I should see message "Your member information has been successfully saved."

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

test_user_email = "test03@example.com"
test_user_password = "123456"
new_first_name = "CCC" #Change it before test
new_last_name = "DDD" #Change it before test

## open browser and login page
driver = webdriver.Chrome()
driver.get("http://mb.test.ingenio.com/index.html#/login")

wait = WebDriverWait(driver, 10)
user_name_field = wait.until(EC.element_to_be_clickable((By.ID, "userName")))
user_name_field.send_keys(test_user_email)

password_field = driver.find_element_by_id("password")
password_field.send_keys(test_user_password)

login_button = driver.find_element_by_id("btnLogin")
login_button.click()

#time.sleep(5)

common_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
common_menu.click()

user_name = wait.until(EC.element_to_be_clickable((By.ID, "mn-member-name")))
user_name.click()

first_name_field = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
first_name_field.clear()
first_name_field.send_keys(new_first_name)

last_name_field = driver.find_element_by_id("last-name")
last_name_field.clear()
last_name_field.send_keys(new_last_name)

save_button = driver.find_element_by_id("btn-save")
save_button.click()

try:
    success_message = wait.until(EC.element_to_be_clickable((By.ID, "msg-result")))
    assert "successfully" in success_message.text

finally:
    driver.quit()


