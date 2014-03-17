from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#testing data
test_user_email = "test01@example.com"
test_user_password = "123456"
test_user_name = "Member4760"

driver = webdriver.Chrome()
driver.get("http://mb.test.ingenio.com/index.html")
#print "getting is done"

wait = WebDriverWait(driver, 100)
toggle_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
toggle_menu.click()
# print toggle_menu

elem = driver.find_element_by_class_name("menu-text-pos")
elem.click()

name_field = wait.until(EC.element_to_be_clickable((By.ID, "userName")))
name_field.send_keys(test_user_email)

password_field = driver.find_element_by_id("password")
password_field.send_keys(test_user_password)

login_button = driver.find_element_by_id("btnLogin")
login_button.click()

common_menu = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "show-menu-button")))
common_menu.click()


user_login = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "menu-text-pos")))
assert test_user_name in user_login.text
print "Test complete successfully"
driver.quit()