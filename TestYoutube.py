from pandas import options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.youtube.com/")

time .sleep(2)

search_box = driver.find_element(By.XPATH, "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
search_box.send_keys("Selenium Python")
search_Button = driver.find_element(By.XPATH, "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button")
search_Button.click()

time .sleep(2)

results = driver.find_elements(By.XPATH, "//a[@href]")
for result in results:
    print(result.get_attribute("href"))

time .sleep(2)
driver.quit()