

def find_city(city_list: list):

    for city in city_list:
        print(city['name'])

        for key, value in city['weather'].items():
            # print(f"{key}: {value}")

            if key == 'temperature' and value > 15:
                return None  # print(f"{key}: {value}")
                break


cities = [
    {
        'name': 'London',
        'weather': {
            'condition': 'raining',
            'temperature': 10
        }
    },
    {        'name': 'Munich',
        'weather': {
            'condition': 'sunny',
            'temperature': 12
        }
    },
    {
        'name': 'Tel-Aviv',
        'weather': {
            'condition': 'sunny',
            'temperature': 25
        }
    },
    {
        'name': 'Chelyabinsk',
        'weather': {
            'condition': 'snow',
            'temperature': -5
        }
    },
]

find_city(cities)