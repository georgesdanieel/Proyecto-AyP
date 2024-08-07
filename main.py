import requests
import json
from film import Film 
from character import Character
from planet import Planet
from species import Species
from vehicle import Vehicle
from starship import Starship
from stats import *
from missions import *

def load_homeworld_name(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['result']['properties']['name']
    return "Unknown"
def load_entity_names(urls):
    names = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        names.append(data['result']['properties']['name'])
    return names
def convert_to_number(value, dtype=float):
    """ Intenta convertir un valor a un tipo numérico dado, maneja excepciones y valores especiales. """
    if value.lower() == 'unknown':
        return None
    try:
        value = value.replace(',', '')
        return dtype(value)
    except ValueError:
        return None