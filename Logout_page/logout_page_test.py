from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#open brouser and testing page
driver = webdriver.Chrome()
driver.get("http://keen-mobile-bootstrap.stage.ingenio.com/#/login")

#login user
wait = WebDriverWait(driver, 10)
name_field = wait.until(EC.element_to_be_clickable((By.ID, "userName")))
name_field.send_keys("igorattest")

password_field = driver.find_element_by_id("password")
password_field.send_keys("igor12")

login_button = driver.find_element_by_id("btnLogin")
login_button.click()

#open menu
toggle_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
toggle_menu.click()

#logout user
logout_user = wait.until(EC.element_to_be_clickable((By.ID, "logout")))
print logout_user.text

#logout
#assert logout
#close brouser