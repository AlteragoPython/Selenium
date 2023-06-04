from selenium import webdriver
from selenium.webdriver.common.by import By


class Base_page:
    driver = webdriver.Chrome()
    url = 'https://www.saucedemo.com/'
    driver.get(url)



class Locators:
    Username_field = (By.NAME,'user-name')
    Password_field = (By.XPATH,'//*[@id="password"]')
    Login_button = (By.ID,'login-button')

