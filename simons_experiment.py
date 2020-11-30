from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import coordinates_handler as ch
import json
import result_saver


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
    time.sleep(1)


def main():
    driver = load_selenium()
    book = ch.load_coordinates('Coordinates.xlsx')
    tables = ch.book_to_table(book)
    for party_name in tables.keys():
        print("p:", party_name)
        party = tables.get(party_name)
        for index in party.index:
            municipality = party['Municipality'][index]
            coordinates = json.loads(party['aggregate'][index])
            name = party_name + ' - ' + municipality + '.txt'
            folder_path = 'Query_Results/Europa/'
            cmd_name = "Emulation.setGeolocationOverride"
            driver.execute_cdp_cmd(cmd_name, coordinates)
            browse(driver)
            result_saver.result_saver(driver, folder_path, name)
    driver.close()


if __name__ == '__main__':
    main()
