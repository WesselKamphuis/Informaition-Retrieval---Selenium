def result_saver(driver):
    f = open('search_results.txt',"a")
    links = driver.find_elements_by_css_selector(".r a")
    for link in links:
      a = link.get_attribute('href')
      f.write( a + '\n')
    f.close()
