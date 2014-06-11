
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class KeenMobileUser:
    def __init__(self, driver):
        self.driver = driver


    def open_tested_site(self, tested_link):

        self.driver.get(tested_link)
        #print "getting is done"

    def close_site(self):
        time.sleep(5)
        self.driver.quit()

    def register(self, email, password, confirm_password):
        #print ("Registrate with email - %s password - %s and confirm password - %s" % (email, password, confirm_password))
        wait = WebDriverWait(self.driver, 100)
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "regEmail")))
        email_field.send_keys(email)

        password_field = self.driver.find_element_by_id("regPassword")
        password_field.send_keys(password)

        confirm_password_field = self.driver.find_element_by_id("regPassword2")
        confirm_password_field.send_keys(confirm_password)

        register_button = self.driver.find_element_by_id("btnRegister")
        register_button.click()


    def login_by_email(self, email, password):
        #print ("Login with email - %s password - %s and confirm password - %s" % (email, password, confirm_password))

        wait = WebDriverWait(self.driver, 100)
        toggle_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
        toggle_menu.click()
        # print toggle_menu

        elem = self.driver.find_element_by_class_name("menu-text-pos")
        elem.click()

        name_field = wait.until(EC.element_to_be_clickable((By.ID, "userName")))
        name_field.clear()
        name_field.send_keys(email)

        password_field = self.driver.find_element_by_id("password")
        password_field.send_keys(password)

        login_button = self.driver.find_element_by_id("btnLogin")
        login_button.click()

    def login_by_name(self, password):
        #print ("Login with email - %s password - %s and confirm password - %s" % (email, password, confirm_password))

        wait = WebDriverWait(self.driver, 100)
        toggle_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
        toggle_menu.click()
        # print toggle_menu

        elem = self.driver.find_element_by_class_name("menu-text-pos")
        elem.click()

        password_field = wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_field.send_keys(password)

        login_button = self.driver.find_element_by_id("btnLogin")
        login_button.click()

    def logout(self):
        #open menu
        wait = WebDriverWait(self.driver, 100)
        toggle_menu = wait.until(EC.element_to_be_clickable((By.ID, "toggle-menu")))
        toggle_menu.click()

        #logout user
        logout_user = wait.until(EC.element_to_be_clickable((By.ID, "mn-logout")))
        print(logout_user)
        logout_user.click()

    def fill_first_name(self, first_name):
        print ("First name")

    def fill_last_name(self, last_name):
        print ("Last name")

    def change_member_name(self, member_name):
        print ("Member name")

    def change_first_name(self, first_name):
        print ("First name")

    def change_last_name(self, last_name):
        print ("Last name")

    def change_email(self, email):
        print ("Email")

    def change_password(self, password):
        print ("Password")



new_user = KeenMobileUser(webdriver.Chrome())

test_user_email = "test01@example.com"
test_user_password = "123456"
test_user_name = "Member498744"

test_register_email = "test05@example.com"
test_register_password = "123456"
test_register_confirm_password = "123456"

login_link = "http://m.keen.com/"
register_link = "http://m.keen.com/#/register"

#new_user.open_tested_site(login_link)
#new_user.login_by_email(test_user_email, test_user_password)
#new_user.logout()

new_user.open_tested_site(register_link)
new_user.register(test_register_email, test_register_password, test_register_confirm_password)
new_user.logout()
#new_user.login_by_email(test_register_email, test_user_password)
new_user.login_by_name(test_register_password)
new_user.logout()

new_user.close_site()
