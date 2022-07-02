import requests


class SuperHero:
    def __init__(self, name):
        self.url = 'https://akabab.github.io/superhero-api/api/all.json'
        self.headers = {'Content-Type': 'application/json'}
        self.name = name

    def _get_super_hero_list(self):
        response = requests.get(url=self.url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("There's no hope as there's no Super Heroes left.")

    def _get_superhero_id(self):
        super_heroes = self._get_super_hero_list()
        for items in super_heroes:
            if self.name == items['name']:
                return items['id']

    def get_superhero_intelligence(self):
        super_hero_id = self._get_superhero_id()
        self.url = f'https://akabab.github.io/superhero-api/api/powerstats/{super_hero_id}.json'
        response = requests.get(url=self.url, headers=self.headers)
        response = response.json()
        return response['intelligence']


super_heroes_list = ['Hulk', 'Captain America', 'Thanos']
super_heroes_dict = {}
for hero_name in super_heroes_list:
    some_hero = SuperHero(name=hero_name)
    super_heroes_dict[hero_name] = f'{some_hero.get_superhero_intelligence()}'


def the_most_intelligent(dictionary):
    for key, value in dictionary.items():
        dictionary[key] = int(value)
    return max(dictionary, key=dictionary.get)


print(f'The most intelligent Super Hero occurred {the_most_intelligent(super_heroes_dict)}')
print(f'Whose intelligence is {super_heroes_dict[the_most_intelligent(super_heroes_dict)]}!!!')
