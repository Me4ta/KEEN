from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://keen-mobile-bootstrap.stage.ingenio.com/")
#print "getting is done"

wait = WebDriverWait(driver, 100)
toggle_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
toggle_menu.click()
# print toggle_menu

elem = driver.find_element_by_class_name("menu-text-pos")
elem.click()

name_field = wait.until(EC.element_to_be_clickable((By.ID, "userName")))
#print name_field
name_field.send_keys("igorattest")

password_field = driver.find_element_by_id("password")
password_field.send_keys("igor12")

login_button = driver.find_element_by_id("btnLogin")
login_button.click()

#click confirm
#assert login 
# driver.close() 
#driver.quit()