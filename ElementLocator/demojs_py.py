import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    class DemoJs():
        def demo_js(self):
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            #driver.get("https://www.rcvacademy.com/")
            driver.execute_script("window.open('https://training.rcvacademy.com/login', '_self');")
            demo_element = driver.execute_script("return document.getElementById('login');")
            driver.execute_script("arguments[0].click();", demo_element)

    ss = DemoJs()
    ss.demo_js()

except Exception as e:
    print(e)
