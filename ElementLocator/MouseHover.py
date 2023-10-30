import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    class DemoMouseHover():
        def demo_hover(self):
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://www.yatra.com")
            more_button = driver.find_element(By.XPATH, "//span[@class='more-arr']")
            ActionChains(driver).move_to_element(more_button).perform()
            driver.find_element(By.XPATH, "//span[normalize-space()='Monuments']").click()

    mouse_hover = DemoMouseHover()
    mouse_hover.demo_hover()

except Exception as e:
    print(e)
