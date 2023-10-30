import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    class DemoFindByText():
            def locate_by_text(self):
                options = webdriver.ChromeOptions()
                options.add_experimental_option("useAutomationExtension", False)
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                options.add_experimental_option("detach", True)
                driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
                driver.maximize_window()
                driver.get("https://www.hotels.com")
                text = driver.find_element(By.XPATH, "//div[@aria-label='2 out of 7']//div//a[@class='uitk-card-link']").get_property("value")
                text2 = driver.find_element(By.XPATH,
                                           "//div[@aria-label='1 out of 7']//div//div[@class='uitk-layout-position uitk-layout-position-relative']//button[@type='button']").get_attribute("type")
            

    findbyid = DemoFindByText()
    findbyid.locate_by_text()

except Exception as e:
    print(e)
