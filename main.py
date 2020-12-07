from Experiment import browser


def main():
    dict_of_queries = {
        'Restaurant_Near_Me': 'restaurant near me',
        'Belastingen': 'belastingen',
        'Defensie': 'defensie',
        'Europese_Unie': 'europese unie',
        'Klimaat': 'klimaat',
        'Onderwijs': 'onderwijs',
        'Vluchtelingen': 'vluchtelingen',
        'Zorg': 'zorg'}

    for key in dict_of_queries.keys():
        if key == 'Restaurant_Near_Me':
            query = 'restaurant near me'
        else:
            query = 'partijbeleid ' + dict_of_queries.get(key)
        browser.browser(query, key)


if __name__ == '__main__':
    main()
