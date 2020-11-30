def result_saver(driver, folder_path, name):
    f = open((folder_path+name), "a")
    links = driver.find_elements_by_css_selector(".rc a")
    for link in links:
        a = link.get_attribute('href')
        f.write(a + '\n')
    f.close()
