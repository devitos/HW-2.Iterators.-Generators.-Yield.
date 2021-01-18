import requests


class MyIterator:

    def __init__(self, url):
        self.n = -1
        self.url = url
        response = requests.get(self.url)
        self.country_file = response.json()

    def __iter__(self):
        return self

    def __next__(self):
        a = dict()
        self.n += 1
        if self.n >= len(self.country_file):
            raise StopIteration
        wiki_en = 'https://en.wikipedia.org/wiki/'
        en_name = self.country_file[self.n]['name']['official']
        country_url_en = wiki_en + en_name.replace(' ', '_')
        a[en_name] = country_url_en
        with open('wiki_country.txt', 'a', encoding='UTF-8') as f:
            f.write(f'{en_name}: \n{country_url_en} \n')
        return a


if __name__ == '__main__':

    iterator = MyIterator('https://raw.githubusercontent.com/mledoze/countries/master/countries.json')

    for country in iterator:
        print(country)
