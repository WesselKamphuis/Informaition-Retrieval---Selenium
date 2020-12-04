def result_saver(driver, folder_path, name):
    f = open((folder_path+name), "a")
    links = driver.find_elements_by_css_selector(".rc a")
    spam1 = 'https://webcache.googleusercontent.com'
    spam2 = 'https://www.google.com'
    spam3 = 'https://translate.google.com'
    for link in links:
        a = link.get_attribute('href')
        if (spam1 not in a) and (spam2 not in a) and (spam3 not in a):
            f.write(a + '\n')
    f.close()
