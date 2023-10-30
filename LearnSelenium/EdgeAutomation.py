from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By



options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))

driver.maximize_window()
driver.get("https://www.facebook.com/")


element = driver.find_element(By.XPATH, "//input[@id='email']")
element.clear()
element.send_keys("tysonleisiano@gmail.com")


element_password = driver.find_element(By.XPATH, "//input[@id='pass']")
element_password.clear()
element_password.send_keys("Leisiano08!")


login_button_element = driver.find_element(By.NAME, "login")
login_button_element.click()



