from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.facebook.com/")

element = driver.find_element(By.ID, "email")
element.clear()
element.send_keys("tysonleisiano@gmail.com")

element_password = driver.find_element(By.ID, "pass")
element_password.clear()
element_password.send_keys("Leisiano08!")


login_button_element = driver.find_element(By.NAME, "login")
login_button_element.click()


