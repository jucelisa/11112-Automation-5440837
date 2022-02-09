from pandas import options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.com/")

time .sleep(2)

element = driver.find_element(By.NAME, "q")
element.send_keys("Selenium Python")
element.submit()

time .sleep(2)

results = driver.find_elements(By.XPATH, "//a[@href]")
for result in results:
    print(result.get_attribute("href"))

time .sleep(2)
driver.quit()