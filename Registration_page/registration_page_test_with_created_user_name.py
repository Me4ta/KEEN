from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


## !!! change test_user_email (+1) before start the test

test_user_email = "test30@example.com"
test_user_password = "123456"

## open browser and registration page
driver = webdriver.Chrome()
driver.get("http://mb.test.ingenio.com/index.html#/register")

## input e-mail, password, confirm password
wait = WebDriverWait(driver, 10)
email_field = wait.until(EC.element_to_be_clickable((By.ID, "regEmail")))
email_field.send_keys(test_user_email)

password_field = driver.find_element_by_id("regPassword")
password_field.send_keys(test_user_password)

confirm_password_field = driver.find_element_by_id("regPassword2")
confirm_password_field.send_keys(test_user_password)

register_button = driver.find_element_by_id("btnRegister")
register_button.click()

## make a logout
common_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
common_menu.click()

logout_button = wait.until(EC.element_to_be_clickable((By.ID, "mn-logout")))
user = driver.find_element_by_class_name("menu-text-pos")
user_name = user.text
logout_button.click()

## login with created user name and password
common_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
common_menu.click()

login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "menu-text-pos")))
login_button.click()

name_field = wait.until(EC.element_to_be_clickable((By.ID, "userName")))
name_field.send_keys(user_name)

password_field = wait.until(EC.element_to_be_clickable((By.ID, "password")))
password_field.send_keys(test_user_password)

login_button = driver.find_element_by_id("btnLogin")
login_button.click()

## assert login
common_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
common_menu.click()

try:
    user_menu = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"menu-text-pos"), "Member"))
    logged_in_user = driver.find_element_by_class_name("menu-text-pos")

    assert user_name in logged_in_user.text

    ## logout
    logout_user = wait.until(EC.element_to_be_clickable((By.ID, "mn-logout")))
    logout_user.click()

    print "Test complete successfully"
finally:
    driver.quit()