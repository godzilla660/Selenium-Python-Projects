import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    class SwitchingWindows():
        def switch_windows(self):
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://www.yatra.com/")
            driver.find_element(By.XPATH, "//a[@title='Niyo Global']//img[@class='conta iner large-banner']").click()
            parent_window = driver.current_window_handle
            all_handles = driver.window_handles
            print(all_handles)
            for handle in all_handles:
                if handle != parent_window:
                    driver.switch_to.window(handle)
                    driver.find_element(By.XPATH, "//input[@id='firstnamecor']").send_keys("Tyson")
                    driver.find_element(By.XPATH, "//input[@id='emailcor']").send_keys("tysonleisiano@gmail.com")
                    driver.find_element(By.XPATH, "//input[@id='mobile_no']").send_keys("0718885134")
                    driver.find_element(By.XPATH, "//button[@id='send_otp']").click()
                    #driver.find_element(By.XPATH, "//button[@id='contact_formcor']").click()

            #driver.switch_to.window(parent_window)
            #driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']")

    sw = SwitchingWindows()
    sw.switch_windows()

except Exception as e:
    print(e)
