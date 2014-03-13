from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# open browser and registration page
driver = webdriver.Chrome()
driver.get("http://mb.test.ingenio.com/index.html#/register")

# input e-mail, password, confirm password
wait = WebDriverWait(driver, 10)
email_field = wait.until(EC.element_to_be_clickable((By.ID, "regEmail")))
test_user_email = "test04@example.com"
email_field.send_keys(test_user_email)

password_field = driver.find_element_by_id("regPassword")
password_field.send_keys("123456")

confirm_password_field = driver.find_element_by_id("regPassword2")
confirm_password_field.send_keys("123456")

register_button = driver.find_element_by_id("btnRegister")
register_button.click()

# save the created name
common_menu = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "show-menu-button")))
common_menu.click()

# make a logout
logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logout")))
logout_button.click()

# login with created name and password
common_menu = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "show-menu-button")))
common_menu.click()

# assert login
# logout
#deiver.quit()