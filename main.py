import requests


def print_weather():
    url_template = 'https://wttr.in/{}'

    payload = {
        'n': '',
        'T': '',
        'q': '',
        'm': '',
        'M': '',
        '&': '',
        'lang': 'ru'
    }

    locations = ['Лондон', 'Шереметьево', 'Череповец']

    for location in locations:
        url = url_template.format(location)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    print_weather()
