from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    class FacebookAutomation():
        def facebook_automation(self):
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://www.facebook.com/")

            driver.find_element(By.XPATH, "//button[contains(text(), 'Accept all cookies')]").click()

            driver.find_element(By.ID, "email").send_keys("tysonleisiano@gmail.com")
            driver.find_element(By.ID, "email").send_keys("Leisiano08!")
            login_button_element = driver.find_element(By.NAME, "login")
            driver.find_element(By.XPATH, "//span[contains(text(),'Memories')]")

            login_button_element.click()

    automate = FacebookAutomation()
    automate.facebook_automation()
except Exception as e:
        print(e)
