from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# open browser and registration page
driver = webdriver.Chrome()
driver.get("http://mb.test.ingenio.com/index.html#/register")

# input e-mail, password, confirm password
# save the created name
# make a logout
# login with created name and password
# assert login
# logout
#deiver.quit()