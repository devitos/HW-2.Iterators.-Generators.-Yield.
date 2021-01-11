def create_urlfile():
    import json
    import requests
    import pprint

    a = dict()
    response = requests.get('https://raw.githubusercontent.com/mledoze/countries/master/countries.json')
    beta_file = response.json()
    # Не понял почему к этому файлу нельзя применить команду json.load.
    # json.load(beta_file)
    wiki_en = 'https://en.wikipedia.org/wiki/'
    wiki_ru = 'https://ru.wikipedia.org/wiki/'

    countries = (country for country in beta_file)

    with open('wiki_country.txt', 'w', encoding='UTF-8') as f:
        for country in countries:
            ru_name = country['translations']['rus']['official']
            en_name = country['name']['official']
            country_url_en = wiki_en + en_name.replace(' ', '_')
            country_url_ru = wiki_ru + ru_name.replace(' ', '_')
            f.write(f'{ru_name}: \n{country_url_en} \n{country_url_ru} \n')
            a[ru_name] = country_url_en + ' '
            a[ru_name] += country_url_ru
    pprint.pprint(a)
    return


create_urlfile()
