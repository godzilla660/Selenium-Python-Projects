import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


try:
    class DemoScreenshot():
        def screenshot_demo(self):
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://www.facebook.com/")
            screenshot = driver.find_element(By.NAME, "login")
            screenshot.save_screenshot(".\\test.png")
            screenshot.click()
            time.sleep(3)
            driver.get_screenshot_as_file(".\\test1.png")


    ss = DemoScreenshot()
    ss.screenshot_demo()

except Exception as e:
    print(e)
