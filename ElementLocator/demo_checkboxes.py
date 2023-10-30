import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    class DemoCheckBoxes():
            def checkbox_demo(self):
                options = webdriver.ChromeOptions()
                options.add_experimental_option("useAutomationExtension", False)
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                options.add_experimental_option("detach", True)
                driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
                driver.maximize_window()
                driver.get("https://www.sugarcrm.com/au/request-demo/")
                driver.find_element(By.ID, "CybotCookiebotDialogBodyUnderlay").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "//input[@id='doi0']").click()

    findbyid = DemoCheckBoxes()
    findbyid.checkbox_demo()

except Exception as e:
    print(e)
