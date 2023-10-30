from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    class DemoDropdown():
        def dropdown_demo(self):
            options = webdriver.ChromeOptions()
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")

            dropdown = Select(driver.find_element(By.ID, "course"))

            dropdown.select_by_index(1)
            time.sleep(2)
            dropdown.select_by_index(2)
            time.sleep(2)
            dropdown.select_by_index(3)
            time.sleep(2)
            dropdown.select_by_index(4)
            time.sleep(2)

    dd = DemoDropdown()
    dd.dropdown_demo()

except Exception as e:
    print(e)

