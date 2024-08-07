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
def load_films_from_api():
    api_url = "https://www.swapi.tech/api/films"
    response = requests.get(api_url)
    data = response.json()
    for film_data in data['result']:
        # Cargar los nombres de las entidades relacionadas
        characters = load_entity_names(film_data['properties']['characters'])
        starships = load_entity_names(film_data['properties']['starships'])
        vehicles = load_entity_names(film_data['properties']['vehicles'])
        species = load_entity_names(film_data['properties']['species'])
        planets = load_entity_names(film_data['properties']['planets'])
        
        film = Film(
            title=film_data['properties']['title'],
            episode_id=film_data['properties']['episode_id'],
            opening_crawl=film_data['properties']['opening_crawl'],
            director=film_data['properties']['director'],
            producer=film_data['properties']['producer'],
            release_date=film_data['properties']['release_date'],
            species=species,
            starships=starships,
            vehicles=vehicles,
            characters=characters,
            planets=planets,
            url=film_data['properties']['url'],
            created=film_data['properties']['created'],
            edited=film_data['properties']['edited']
        )
        Film.film_list.append(film)
def load_character_from_api():
    api_url = "https://www.swapi.tech/api/people"
    while api_url:  # Loop para manejar la paginación
        response = requests.get(api_url)
        data = response.json()
        for character_data in data['results']:  # Uso de la clave correcta 'results'
            # Cargar las URLs para cada personaje para obtener más detalles
            character_detail_response = requests.get(character_data['url'])
            character_detail = character_detail_response.json()['result']['properties']
            
            # Obtener el nombre del homeworld del personaje
            if character_detail['homeworld']:
                homeworld_response = requests.get(character_detail['homeworld'])
                homeworld_data = homeworld_response.json()['result']['properties']
                homeworld_name = homeworld_data['name']
            else:
                homeworld_name = "Unknown"  # Si no hay URL del homeworld, asignar un valor por defecto