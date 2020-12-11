from Experiment import browser


def main():
    dict_of_queries = {
        'Restaurant_Near_Me': 'restaurant near me',
        'Pensioenen': 'pensioenen',
        'Veiligheid': 'veiligheid',
        'Europese_Unie': 'europese unie',
        'Klimaat': 'klimaat',
        'Onderwijs': 'onderwijs',
        'Immigratie': 'immigratie',
        'Werkgelegenheid': 'werkgelegenheid',
        'Corona_aanpak': 'corona aanpak',
        'Woningbouw': 'woningbouw',
        'Zorg': 'zorg'}

    for key in dict_of_queries.keys():
        if key == 'Restaurant_Near_Me':
            query = 'restaurant near me'
        else:
            query = 'standpunten ' + dict_of_queries.get(key)
        browser.browser(query, key)


if __name__ == '__main__':
    main()
