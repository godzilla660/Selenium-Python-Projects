from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    class AutoSuggest():
        def autosuggest_demo(self):
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://www.yatra.com/holidays")
            driver.find_element(By.XPATH, "//input[@id='BE_holiday_leaving_city']").send_keys("New")
            time.sleep(30)
            search_results = driver.find_elements(By.XPATH, "(//input[@id='BE_holiday_leaving_city'])[1]]")
            for result in search_results:
                if "New Delhi" in result.text:
                    result.click()
                    break

            driver.find_element(By.XPATH, "//td[@id='30/10/2023']").click()
            driver.find_element(By.XPATH, "//td[@id='16/11/2023']//span[@class='price'][normalize-space()='5,387']").click()

    dd = AutoSuggest()
    dd.autosuggest_demo()

except Exception as e:
    print(e)
