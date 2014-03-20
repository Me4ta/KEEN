from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

test_user_email = "test01@example.com"
test_user_password = "123456"
test_user_name = "Member4760"


#open browser and testing page
driver = webdriver.Chrome()
driver.get("http://mb.test.ingenio.com/index.html#/login")

#login user
wait = WebDriverWait(driver, 10)
name_field = wait.until(EC.element_to_be_clickable((By.ID, "userName")))
name_field.send_keys(test_user_email)

password_field = driver.find_element_by_id("password")
password_field.send_keys(test_user_password)

login_button = driver.find_element_by_id("btnLogin")
login_button.click()

#open menu
toggle_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
toggle_menu.click()

#logout user
logout_user = wait.until(EC.element_to_be_clickable((By.ID, "mn-logout")))
logout_user.click()

#assert logout
try:
    common_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
    common_menu.click()
    login_menu = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "menu-text-pos")))
    assert "Log In" in login_menu.text
    print "Test complete successfully"
finally:
    driver.quit()