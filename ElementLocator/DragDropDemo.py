import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    class DemoDragDrop():
        def drag_drop(self):
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://jqueryui.com/droppable")
            driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
            element_1 = driver.find_element(By.XPATH, "//div[@id='draggable']")
            element_2 = driver.find_element(By.XPATH, "//div[@id='droppable']")
            ActionChains(driver).drag_and_drop(element_1, element_2).perform()
            time.sleep(3)

    drag = DemoDragDrop()
    drag.drag_drop()

except Exception as e:
    print(e)
