from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    class Multi_Select():
        def multiselect_demo(self):
            options = webdriver.ChromeOptions()
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")

            dropdown = Select(driver.find_element(By.ID, "ide"))

            dropdown.select_by_visible_text("Eclipse")
            time.sleep(2)
            dropdown.select_by_visible_text("IntelliJ IDEA")
            time.sleep(2)
            dropdown.select_by_visible_text("Visual Studio")
            time.sleep(2)
            dropdown.select_by_visible_text("NetBeans")
            time.sleep(2)

    dd = Multi_Select()
    dd.multiselect_demo()

except Exception as e:
    print(e)

