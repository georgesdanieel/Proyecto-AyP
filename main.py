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

            # Crear instancia de Character con los datos disponibles, incluyendo el nombre del homeworld
            character = Character(
                name=character_detail['name'],
                birth_year=character_detail['birth_year'],
                eye_color=character_detail['eye_color'],
                gender=character_detail['gender'],
                hair_color=character_detail['hair_color'],
                height=character_detail['height'],
                mass=character_detail['mass'],
                skin_color=character_detail['skin_color'],
                homeworld=homeworld_name,  # Usar el nombre del homeworld
                url=character_detail['url'],
                created=character_detail['created'],
                edited=character_detail['edited']
            )
            Character.character_list.append(character)

        api_url = data.get('next', None)  # Actualizar el URL para la siguiente página
def load_planets_from_api():
    api_url = "https://www.swapi.tech/api/planets"
    while api_url:  # Loop para manejar la paginación
        response = requests.get(api_url)
        data = response.json()
        for planet_data in data['results']:  # Usamos la clave 'results' para iterar
            # Cargar las URLs para cada planeta para obtener más detalles
            planet_detail_response = requests.get(planet_data['url'])
            planet_detail = planet_detail_response.json()['result']['properties']

            # Crear instancia de Planet con los datos disponibles
            planet = Planet(
                name=planet_detail['name'],
                diameter=planet_detail['diameter'],
                rotation_period=planet_detail['rotation_period'],
                orbital_period=planet_detail['orbital_period'],
                gravity=planet_detail['gravity'],
                population=planet_detail['population'],
                climate=planet_detail['climate'],
                terrain=planet_detail['terrain'],
                surface_water=planet_detail['surface_water'],
                url=planet_detail['url'],
                created=planet_detail['created'],
                edited=planet_detail['edited']
            )
            Planet.planet_list.append(planet)

        api_url = data['next']  # Actualizar el URL para la siguiente página
def load_vehicles_from_api():
    api_url = "https://www.swapi.tech/api/vehicles"
    while api_url:  # Loop para manejar la paginación
        response = requests.get(api_url)
        data = response.json()
        for vehicle_data in data['results']:  # Usamos la clave 'results' para iterar
            # Cargar las URLs para cada vehículo para obtener más detalles
            vehicle_detail_response = requests.get(vehicle_data['url'])
            vehicle_detail = vehicle_detail_response.json()['result']['properties']
            
            # Cargar los nombres de films y pilotos si existen
            films_names = load_entity_names(vehicle_detail['films']) if 'films' in vehicle_detail else []
            pilots_names = load_entity_names(vehicle_detail['pilots']) if 'pilots' in vehicle_detail else []


            # Crear instancia de Vehicle con los datos disponibles
            vehicle = Vehicle(
                name=vehicle_detail['name'],
                model=vehicle_detail['model'],
                vehicle_class=vehicle_detail['vehicle_class'],
                manufacturer=vehicle_detail['manufacturer'],
                cost_in_credits=vehicle_detail['cost_in_credits'],
                length=vehicle_detail['length'],
                crew=vehicle_detail['crew'],
                passengers=vehicle_detail['passengers'],
                max_atmosphering_speed=vehicle_detail['max_atmosphering_speed'],
                cargo_capacity=vehicle_detail['cargo_capacity'],
                consumables=vehicle_detail['consumables'],
                films=films_names,  # Usamos los nombres cargados
                pilots=pilots_names,  # Usamos los nombres cargados
                url=vehicle_detail['url'],
                created=vehicle_detail['created'],
                edited=vehicle_detail['edited']
            )
            Vehicle.vehicle_list.append(vehicle)

        api_url = data['next']  # Actualizar el URL para la siguiente página
def load_starships_from_api():

    api_url = "https://www.swapi.tech/api/starships"
    while api_url:
        response = requests.get(api_url)
        data = response.json()
        for starship_data in data['results']:
            starship_detail_response = requests.get(starship_data['url'])
            starship_detail = starship_detail_response.json()['result']['properties']

            # Utilizar la función auxiliar para convertir y manejar valores
            starship = Starship(
                name=starship_detail['name'],
                model=starship_detail['model'],
                starship_class=starship_detail['starship_class'],
                manufacturer=starship_detail['manufacturer'],
                cost_in_credits=convert_to_number(starship_detail['cost_in_credits'], int),
                length=convert_to_number(starship_detail['length'], int),
                crew=starship_detail['crew'],
                passengers=convert_to_number(starship_detail['passengers'], int),
                max_atmosphering_speed=convert_to_number(starship_detail['max_atmosphering_speed'], int),
                hyperdrive_rating=convert_to_number(starship_detail['hyperdrive_rating'], float),
                MGLT=convert_to_number(starship_detail['MGLT'], int),
                cargo_capacity=convert_to_number(starship_detail['cargo_capacity'], int),
                consumables=starship_detail['consumables'],
                pilots=load_entity_names(starship_detail['pilots']),
                url=starship_detail['url'],
                created=starship_detail['created'],
                edited=starship_detail['edited']
            )
            Starship.starship_list.append(starship)

        api_url = data.get('next')  # Actualizar el URL para la siguiente página
def load_species_from_api():
    api_url = "https://www.swapi.tech/api/species"
    while api_url:
        response = requests.get(api_url)
        data = response.json()
        for species_data in data['results']:
            species_detail_response = requests.get(species_data['url'])
            species_detail = species_detail_response.json()['result']['properties']

            # Usar una función auxiliar para cargar los nombres desde los URLs de personas
            people_names = load_entity_names(species_detail['people']) if species_detail['people'] else []
            homeworld_name = load_homeworld_name(species_detail['homeworld']) if species_detail['homeworld'] else "Unknown"

            species=Species(
                name=species_detail['name'], classification=species_detail['classification'], designation=species_detail['designation'],
                average_height=species_detail['average_height'], average_lifespan=species_detail['average_life'], hair_colors=species_detail['hair_color'], 
                skin_colors=species_detail['skin_color'], eye_colors=species_detail['name'], language=species_detail['language'], 
                homeworld=species_detail['homeworld'], people=species_detail['people'], url=species_detail['url'], created=species_detail['created'], 
                edited=species_detail['edited']
            )
            Species.species_list.append(species)
        
        api_url=data.get('next')
def view_movies():
    print("\nLista de películas:")
    for film in Film.film_list:
        print(f"Título: {film.title}, Episode: {film.episode_id}, Fecha de lanzamiento: {film.release_date}, Opening crawl: {film.opening_crawl},
Director: {film.director}")

def view_species():
    print("\nLista de especies:")
    for species in Species.species_list:
        print(f"Título: {species.name}, Altura: {species.average_height}, Clasificación: {species.classification}, Planeta de origen: {species.homeworld},
Lengua Materna: {species.language}")
        
def view_planets():
    print("\nLista de planetas:")
    for planet in Planet.planet_list:
        print(f"Nombre: {planet.title}, Período de órbita: {planet.orbital_period}, Período de rotación: {planet.rotation_period}, Población: {planet.population},
Clima: {planet.climate}")

def search_characters():
    search_query=input("Introduzca parte del nombre del personaje para buscar:  ")
    print("\nResultados de la búsqueda: ")
    for character in Character.character_list:
        if search_query.lower() in character.namemlowe():
            print(f"Nombre: {character.name}, Planeta de origen: {character.homeworld}, Género: {character.gender}")

def submenu():
    while True:
        print("\nSeleccione una opción del submenú:")
        print("1. Película de la saga")
        print("2. Especies de seres vivos")
        print("3. Planetas")
        print("4. Personajes")
        print("5. Regresar al menú principal")

        sub_selec=input(">>> ")
        if sub_selec=="1":
            view_movies()
        elif sub_selec=="2":
            view_species()
        elif sub_selec=="3":
            view_planets()
        elif sub_selec=="4":
            search_characters()
        elif sub_selec=="5":
            print("Regresando al menú principal")
            break
        else: 
            print("Opción no válida. Por favor, intente de nuevo.")

def statistics_submenu():
    while True: 
        print("nSeleccione una opción del submenú de estadísticas:")
        print("1. Gráfico de cantidad de personajes nacidos en cada planeta")
        print("2. Gráficos de características de naves")
        print("3. Estadísticas sobre naves")
        print("4. Regresar al menú principal")

        sub_selec=input(">>> ")
        if sub_selec=="1":
            print("Mostrando gráfico de cantidad de personajes por planeta")
            plot_characters_per_planet(Character.character_list)
        elif sub_selec=="2":
            print("Mostrando gráficos de características de naves")
            plot_starship_characteristics(Starship.starship_list)
        elif sub_selec=="3":
            print("Mostrando estadísticas sobre naves")
            calculate_starship_statistics(Starship.starship_list)
        elif sub_selec=="4":
            print("Regresando al menú principal")
            break
        else: 
            print("Opción no válida. Por favor, intente de nuevo")


def missions_submenu():
    while True:
        print("\nSeleccione una opción del submenú de misiones:")
        print("1. Misiones de la saga")
        print("2. Modificar misión")
        print("3. Visualizar misión")
        print("4. Guardar misiones")
        print("5. Cargar misiones")
        print("6. Regresar al menú principal")

        sub_selec=input(">>> ")

        if sub_selec=="1":
            print("Contruir misión")
            construir_musion()
        elif sub_selec=="2":
            print("Modificar misión")
            modificar_mision()
        elif sub_selec=="3":
            print("Visualizar misión")
            visualizar_mision()
        elif sub_selec=="4":
            print("Guardar misiones")
            guardar_misiones()
        elif sub_selec=="5":
            print("Cargar misiones")
            cargar_misiones()
        elif sub_selec=="6":
            print("Regresando al menú principal")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo")

def main():
    while True:
        print("\nBienvenido a Star Wars Wikis!")
        print("Selecciones que desea realizar:")
        print("1. Ver listado detallados")
        print("2. Ver estadísticas")
        print("3. Ver misiones")
        print("4. Salir")

        selec=input(">>> ")

        if selec=="1":
            submenu()
        elif selec== "2":
            statistics_submenu()
        elif selec=="3":
            missions_submenu()
        elif selec=="4":
            print("Gracias por usar Star Wars Wikis. Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo")

#prin('loading data from swapi...')
#load_films_from_api()
#print("films loaded...")
#load_character_from_api()
#print("characters loaded...")
#load_planets_from_api()
#print("planets loaded...")
#load_starships_from_api()
#print("starships loaded...")
#load_species_from_api()
#print("species loaded...")
#print('Finished loading all apis, starting application...)
#save_data_to_files()
#print("data saved succesfully in txt files")

load_data_from_files()
print('data succesfully loaded from files')
main()








        
         
         