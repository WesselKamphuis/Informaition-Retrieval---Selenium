def result_saver(driver, name):
    f = open(name,"a")
    links = driver.find_elements_by_css_selector(".rc a")
    print("all links: ", links)
    for link in links:
        print("the link: ", link)
        a = link.get_attribute('href')
        f.write( a + '\n')
    f.close()
