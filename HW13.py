from selenium import webdriver
import Locators

driver = webdriver.Chrome()   # create instance of the driver
driver.get("https://www.saucedemo.com/") # go to the website

username_field = driver.find_element(*Locators.Locators.Username_field) # find element username
username_field.clear()
username_field.send_keys("standard_user")