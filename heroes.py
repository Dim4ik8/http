import requests

def get_intelligence(*heroes):
    best_hero = ''
    best_intelligence = 0

    for hero_name in heroes:
        url = 'https://superheroapi.com/api/2619421814940190/search/' + hero_name
        response = requests.get(url)
        # response.json()

        response_data = response.json()
        results = response_data['results']
        # print(results)

        for result in results:
            if result['name'] == hero_name:
                intelligence = result['powerstats']['intelligence']

                if best_hero == '':
                    best_hero = hero_name
                    best_intelligence = int(intelligence)
                if int(intelligence) > best_intelligence:
                    best_hero = hero_name
                    best_intelligence = int(intelligence)

                print(hero_name, ': ', intelligence)

    return best_hero, best_intelligence


print(get_intelligence('Hulk', 'Captain America', 'Thanos'))
