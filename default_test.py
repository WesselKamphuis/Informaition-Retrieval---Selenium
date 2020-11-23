from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.set_window_size(668, 680)
driver.find_element(By.NAME, "q").send_keys("restaurant near me")
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
time.sleep(10)
driver.close()