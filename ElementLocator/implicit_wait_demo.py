import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    class ImplicitWait():
        def implicit_wait(self):
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://login.salesforce.com/?locale=eu")
            driver.find_element(By.XPATH, "//input[@id='username']").send_keys("tysonleisiano@gmail.com")
            driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Leisiano08!")
            driver.find_element(By.XPATH, "//input[@id='Login']").click()


    implicit_w = ImplicitWait()
    implicit_w.implicit_wait()

except Exception as e:
    print(e)
