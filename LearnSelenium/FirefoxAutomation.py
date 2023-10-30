from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()
options.set_preference("detach", True)
driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()
driver.get("https://www.facebook.com/")

element = driver.find_element(By.ID, "email")
element.clear()
element.send_keys("tysonleisiano@gmail.com")

element_pass = driver.find_element(By.ID, "pass")
element_pass.clear()
element_pass.send_keys("Leisiano08!")

login_button_element = driver.find_element(By.NAME, "login")
login_button_element.click()
