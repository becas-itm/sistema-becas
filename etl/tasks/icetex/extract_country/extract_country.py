import os
import json


def extract_country(item: dict):
    if 'country' not in item:
        return item

    item['country'] = get_country(item['country'])

    return item


def get_country(name: str):
    name = name.split(' (')[0].lower()

    country = load_countries().get(name)

    if country:
        return country

    if 'plataforma de educación' in name:
        return {'name': 'Online', 'code': 'ONL'}

    return {'name': 'Otros', 'code': 'OTH'}


countries = None


def load_countries():
    global countries
    if countries is None:
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'countries.json')
        with open(filename, 'r') as file:
            countries = json.loads(file.read())

    return countries
