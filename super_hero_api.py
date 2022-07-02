import requests
from pprint import pprint


class SuperHero:
    def __init__(self):
        self.url = 'https://akabab.github.io/superhero-api/api/all.json'
        self.headers = {'Content-Type': 'application/json'}

    def _get_super_hero_list(self):
        response = requests.get(url=self.url, headers=self.headers)
        if response.status_code == 200:
            #pprint(response.json())
            return response.json()
        else:
            print("There's no hope as there's no Super Heroes left.")

    def _get_superhero_id(self, name):
        super_heroes = self._get_super_hero_list()
        for items in super_heroes:
            if name == items['name']:
                return items['id']

    def _get_superhero_intelligence(self):
        super_hero_id = self._get_superhero_id('Hulk')
        self.url = f'https://akabab.github.io/superhero-api/api/powerstats/{super_hero_id}.json'
        response = requests.get(url=self.url, headers=self.headers)
        response = response.json()
        return response['intelligence']

