from selenium import webdriver
import time

# create webdriver object
chrome = webdriver.Chrome()

# go to website
chrome.get("https://www.google.com/")

# get browser cookie
chrome.get_cookies('foo')

time.sleep(5)
# add_cookie method driver
chrome.add_cookie({"name": "foo", "value": "bar"})


# get all cookies in scope of session
print(chrome.get_cookies())

# delete browser cookie
chrome.delete_cookie("foo")

# clear all cookies in scope of session
chrome.delete_all_cookies()


chrome.close()
