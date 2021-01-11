def create_urlfile():
    import json
    import requests
    import pprint

    a = dict()
    response = requests.get('https://raw.githubusercontent.com/mledoze/countries/master/countries.json')
    beta_file = response.json()
    # Не понял почему к этому файлу нельзя применить команду json.load.
    # json.load(beta_file)
    wiki = 'https://en.wikipedia.org/wiki/'
    countries = (country['name']['official'] for country in beta_file)

    with open('wiki_country.txt', 'w', encoding='UTF-8') as f:
        for country in countries:
            country_url = wiki + country.replace(' ', '_')
            f.write(f'{country}: {country_url}\n')
            a[country] = country_url
    pprint.pprint(a)
    return


create_urlfile()
