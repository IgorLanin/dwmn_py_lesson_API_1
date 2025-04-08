import requests


def main_print_weather():
    url_template = 'https://wttr.in/{}?nTqmM&lang=ru'
    location_1 = 'Лондон'
    location_2 = 'Шереметьево'
    location_3 = 'Череповец'

    url_london = url_template.format(location_1)
    url_svo = url_template.format(location_2)
    url_cherepovec = url_template.format(location_3)

    response_1 = requests.get(url_london)
    response_1.raise_for_status()

    response_2 = requests.get(url_svo)
    response_2.raise_for_status()
    response_3 = requests.get(url_cherepovec)
    response_3.raise_for_status()

    print(response_1.text)
    print(response_2.text)
    print(response_3.text)


if __name__ == '__main__':
    main_print_weather()
