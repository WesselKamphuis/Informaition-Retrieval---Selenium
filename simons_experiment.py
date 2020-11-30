from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import coordinates_handler as ch
import json


def load_selenium():
    driver = webdriver.Chrome()
    return driver


def change_location(driver, coordinates):
    # coordinates = {"latitude": 52.3545828, "longitude": 4.7638762, "accuracy": 1}
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {"latitude": 52.3545828, "longitude": 4.7638762, "accuracy": 1})


def browse(driver):
    driver.get("https://www.google.com/")
    driver.set_window_size(668, 680)
    driver.find_element(By.NAME, "q").send_keys("restaurant near me")
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(2)


def main():
    driver = load_selenium()
    book = ch.load_coordinates('Coordinates.xlsx')
    tables = ch.book_to_table(book)
    vvd = tables.get('VVD')
    vvd_coordinates = vvd['aggregate']
    print(vvd_coordinates)
    for m in vvd_coordinates:
        coordinates = json.loads(m)
        cmd_name = "Emulation.setGeolocationOverride"
        driver.execute_cdp_cmd(cmd_name, coordinates)
        browse(driver)
    driver.close()


if __name__ == '__main__':
    main()
