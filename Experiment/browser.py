import xlrd
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
from Experiment import result_saver


# Load the Chrome Drivers from PATH
def load_selenium():
    driver = webdriver.Chrome()
    return driver


# Uses a method to open an excel file and return the workbook
def load_coordinates(filename):
    wb = xlrd.open_workbook(filename)
    return wb


# converts a workbook into a pandas dataframe for further processing
def book_to_table(book):
    names = book.sheet_names()
    tables = {}
    for name in names:
        tables[name] = pd.read_excel(book, sheet_name=name)
    return tables


# Open the browser on google, enter the query and the delete the cookies
def browse(driver, query):
    driver.get("https://www.google.com/")
    driver.find_element(By.NAME, "q").send_keys(query)
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.delete_all_cookies()


# the Main method
# loads the driver and the input data
def browser(query, directory):
    filename = 'Experiment/Coordinates.xlsx'
    book = load_coordinates(filename)
    tables = book_to_table(book)

    # Every sheet from the input table corresponds to a Political Party
    for party_name in tables.keys():
        party = tables.get(party_name)

        # Every row in the sheet corresponds to: [Municipality], [Percentage], [latitude], [longitude], [aggregate]
        for index in party.index:
            driver = load_selenium()
            municipality = party['Municipality'][index]
            coordinates = json.loads(party['aggregate'][index])

            # The coordinates of the driver are overwritten with the passed values
            cmd_name = "Emulation.setGeolocationOverride"
            driver.execute_cdp_cmd(cmd_name, coordinates)

            # the browse method is called to execute the query
            browse(driver, query)

            # A name is created, stating the name of the party and the municipality
            # the results are then saved using the
            name = party_name + ' - ' + municipality + '.txt'
            folder_path = 'Query_Results/' + directory + '/'
            result_saver.result_saver(driver, folder_path, name)
            driver.close()
