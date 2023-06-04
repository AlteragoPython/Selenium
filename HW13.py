from selenium import webdriver
import Locators

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# find element username
username_field = driver.find_element(*Locators.Locators.Username_field)
username_field.clear()
username_field.send_keys("standard_user")

# find element password
password_field = driver.find_element(*Locators.Locators.Password_field)
password_field.clear()
password_field.send_keys("secret_sauce")

# login to the website
login_button = driver.find_element(*Locators.Locators.Login_button)
login_button.click()

# check  expected URL
current_url = driver.current_url
expected_url = "https://www.saucedemo.com/inventory.html"
assert current_url == expected_url
