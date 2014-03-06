from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
driver.get("http://keen-mobile-bootstrap.test.ingenio.com")
wait = WebDriverWait(driver, 10)
elem = driver.find_element_by_class_name("marginbot15")
assert "Psychic Readings" in elem.text
#click menu
#choose login
#assert new page for login
#input corr name and pass
#click confirm
#assert login
driver.close()