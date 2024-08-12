import requests
import json
import os
import csv
from film import Film 
from character import Character
from planet import Planet
from species import Species
from vehicle import Vehicle
from starship import Starship
from weapons import Weapon
from stats import *
from planet_stats import *
from starship_stats import *
from missions import *


### API loaders
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
    Film.film_list = []
    api_url = "https://www.swapi.tech/api/films"
    response = requests.get(api_url)
    data = response.json()
    for film_data in data['result']:
      
        film = Film(
            title=film_data['properties']['title'],
            episode_id=film_data['properties']['episode_id'],
            opening_crawl=film_data['properties']['opening_crawl'],
            director=film_data['properties']['director'],
            producer=film_data['properties']['producer'],
            release_date=film_data['properties']['release_date'],
            species=film_data['properties']['species'],         # # #
            starships=film_data['properties']['starships'],         # # #
            vehicles=film_data['properties']['vehicles'],         # # #
            characters=film_data['properties']['characters'],         # # #
            planets=film_data['properties']['planets'],         # # #
            url=film_data['properties']['url'],
            created=film_data['properties']['created'],
            edited=film_data['properties']['edited']
        )
        Film.film_list.append(film)
def load_character_from_api():
    Character.character_list = []
    api_url = "https://www.swapi.tech/api/people"
    while api_url:  # Loop para manejar la paginación
        response = requests.get(api_url)
        data = response.json()
        for character_data in data['results']:  # Uso de la clave correcta 'results'
            # Cargar las URLs para cada personaje para obtener más detalles
            character_detail_response = requests.get(character_data['url'])
            character_detail = character_detail_response.json()['result']['properties']     
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
                homeworld=character_detail['homeworld'],  # url homeworld
                url=character_detail['url'],
                weight= None

            )
            Character.character_list.append(character)

        api_url = data.get('next', None)  # Actualizar el URL para la siguiente página
def load_planets_from_api():
    Planet.planet_list = []
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
                edited=planet_detail['edited'],
                films= None,
                residents= None
            )
            Planet.planet_list.append(planet)
        
        api_url = data['next']  # Actualizar el URL para la siguiente página
def load_vehicles_from_api():
    Vehicle.vehicle_list = []
    api_url = "https://www.swapi.tech/api/vehicles"
    while api_url:  # Loop para manejar la paginación
        response = requests.get(api_url)
        data = response.json()
        for vehicle_data in data['results']:  # Usamos la clave 'results' para iterar
            # Cargar las URLs para cada vehículo para obtener más detalles
            vehicle_detail_response = requests.get(vehicle_data['url'])
            vehicle_detail = vehicle_detail_response.json()['result']['properties']
            
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
                films=vehicle_detail['films'],  ###
                pilots=vehicle_detail['pilots'],  ###
                url=vehicle_detail['url'],
                created=vehicle_detail['created'],
                edited=vehicle_detail['edited']
            )
            Vehicle.vehicle_list.append(vehicle)
        
        api_url = data['next']  # Actualizar el URL para la siguiente página
def load_starships_from_api():
    Starship.starship_list = []
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
                pilots=starship_detail['pilots'],
                url=starship_detail['url'],
                created=starship_detail['created'],
                edited=starship_detail['edited'],
                films= None
            )
            Starship.starship_list.append(starship)
        
        api_url = data.get('next')  # Actualizar el URL para la siguiente página
def load_species_from_api():
    Species.species_list = []
    api_url = "https://www.swapi.tech/api/species"
    while api_url:
        response = requests.get(api_url)
        data = response.json()
        for species_data in data['results']:
            species_detail_response = requests.get(species_data['url'])
            species_detail = species_detail_response.json()['result']['properties']
            

            species = Species(
                name=species_detail['name'],
                classification=species_detail['classification'],
                designation=species_detail['designation'],
                average_height=species_detail['average_height'],
                average_lifespan=species_detail['average_lifespan'],
                hair_colors=species_detail['hair_colors'],
                skin_colors=species_detail['skin_colors'],
                eye_colors=species_detail['eye_colors'],
                homeworld=species_detail['homeworld'],
                language=species_detail['language'],
                people=species_detail['people'],
                url=species_detail['url'],
                created=species_detail['created'],
                edited=species_detail['edited']
            )
            Species.species_list.append(species)
        
        api_url = data.get('next')  # Actualizar el URL para la siguiente página

###CSV loaders
def load_characters_from_csv():
    Character.character_list = []
    csv_path = os.path.join(os.path.dirname(__file__), 'csv', 'characters.csv')
    with open(csv_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            character = Character(
                name=row['name'],
                birth_year=row['year_born'],
                eye_color=row['eye_color'],
                gender=row['gender'],
                hair_color=row['hair_color'],
                height=row['height'],
                weight=row['weight']
                mass=None,
                skin_color=row['skin_color'],
                homeworld=row['homeworld'],
                url=None,
            )
            Character.character_list.append(character)
    print('Characters successfully loaded from CSV')
def load_weapons_from_csv():
    Weapon.weapon_list = []
    csv_path = os.path.join(os.path.dirname(__file__), 'csv', 'weapons.csv')
    with open(csv_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            weapon = Weapon(
                weapon_id=row['id'],
                name=row['name'],
                model=row['model'],
                manufacturer=row['manufacturer'],
                cost_in_credits=row['cost_in_credits'],
                length=row['length'],
                weapon_type=row['type'],
                description=row['description'],
                films=row['films'].split(',')  # Assuming films are stored as comma-separated URLs
            )
            Weapon.weapon_list.append(weapon)
    
    print('Weapons successfully loaded from CSV')
def load_planets_from_csv():
    Planet.planet_list = []
    csv_path = os.path.join(os.path.dirname(__file__), 'csv', 'planets.csv')
    with open(csv_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            planet = Planet(
                name=row['name'],
                climate=row['climate'],
                diameter=row['diameter'],
                gravity=row['gravity'],
                orbital_period=row['orbital_period'],
                population=row['population'],
                rotation_period=row['rotation_period'],
                terrain=row['terrain'],
                surface_water=row['surface_water'],
                residents=row['residents'].split(';') if row['residents'] else [],
                films=row['films'].split(';') if row['films'] else [],
                url=None,
                created=None,
                edited=None
            )
            Planet.planet_list.append(planet)
            
    print('Planets successfully loaded from CSV')
def load_starships_from_csv():
    Starship.starship_list=[]
    csv_path= os.path.join(os.path.diname(__file__), 'csv', 'starships.csv')
    with open(csv_path, mode='r', encoding='utf-8') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            starship=Starship(
                name=row['name'],
                model=row['model'],
                manufacturer=row['manufacturer'],
                cost_in_credits=row['cost_in_credits'],
                lenght=row['lenght'],
                max_atmosphering_speed=row['max_atmosphering_speed'],
                crew=row['crew'],
                passengers=row['passengers'],
                cargo_capacity=row['cargo_capacity'],
                consumables=row['consumables'],
                hyperdrive_rating=row['hyperdrive_rating'],
                MGLT=row['MGLT'],
                starship_class=row['starship_class'],
                pilots=row['pilots'],
                films=row['films'],
                url=row['url'],
                created=row['created'],
                edited=row['edited']
                )

            Starship.starship_list.append(starship)
    print('Starship succesfully loaded from CSV')

###Lists     
def view_movies():
    print("\nLista de películas:")
    for film in Film.film_list:
        print(f"Título: {film.title}, Episode: {film.episode_id}, Fecha de lanzamiento: {film.release_date}, Opening crawl: {film.opening_crawl},Director: {film.director}")

def view_species():
    print("\nLista de especies:")
    for species in Species.species_list:
        print("\n\nNombre: {species.name}")
        print(f"Altura: {species.average_height}")
        print(f"Clasificación: {species.classification}")

        homeworld_name="Desconocido"
        for planet in Planet.planet_list:
            if planet.url==species.homeworld:
                homeworld_name=planet.name
                break
        print(f"Origen: {homeworld_name}")
        print(f"Lengua materna: {species.language}")

        character_names=[]
        for person in Character.character_list:
            if person.url in species.people:
                character_names.append(person.name)
        print(f"Personajes: {', '.join(character_names) if character_names else 'Ninguno'}")
    
        films=[]
        for film in Film.film_list:
            if species.url in film.species:
                films.append(f"{film.title}")
        print(f"Películas: {', '.join(film) if film else 'Ninguno'}")

def view_planets():
    print("\nLista de planetas:")
    for planet in Planet.planet_list:
        print(f"Nombre: {planet.name}")
        print(f"Período de órbita: {planet.orbital_period}") 
        print(f"Período de rotación: {planet.rotation_period}") 
        print(f"Población: {planet.population}")
        print(f"Clima: {planet.climate}")

        people_names=[]
        for person in Character.character_list:
            if person.homeworld==planet.url:
                people_names.append(person.name)
        print(f"Personajes: {', '.join(people_names) if people_names else 'Ninguno'}")

        film_titles=[]
        for film in Film.planets:
            if planet.url in film.planets:
                film_titles.append(f"{film.title}")
        print(f"Películas: {', '.join(film_titles) if film_titles else 'Ninguno'}")

def search_characters():
    search_query=input("Introduzca parte del nombre del personaje para buscar:  ")
    print("\nResultados de la búsqueda: ")
    for character in Character.character_list:
        if search_query.lower() in character.name.lower():
            print(f"\n\nNombre: {character.name}")
            print(f"Género: {character.gender}")

            #Finding film titles
            film_titles=[]
            for film in Film.film_list:
                if character.url in film.characters:
                    film_titles.append(f"{film.title}")
            print(f"Películas: {', '.join(film_titles) if film_titles else 'None'}")

            #Finding species name
            species_name="Unknown"
            for species in Species.species_list:
                if character.url in species.people:
                    species_name=species.name
                    break
            print(f"Especies: {species_name}")

            #Finding starship name
            starship_names=[]
            for starship in Starship.starship_list:
                if character.url in starship.pilots:
                    starship_names.append(f"{starship.name}")
            print(f"Naves: {', '.join(starship_names) if starship_names else 'None'}")

            #Finding vehicle name
            vehicles_names=[]
            for film in Film.film_list:
                if character.url in film.vehicles:
                    film_titles.append(f"{film.vehicles}")
            print(f"Vehículos: {', '.join(vehicles_names) if vehicles_names else 'None'}")

### Submenus
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
            planet_graphs()
        elif sub_selec=="2":
            spaceship_graphs()
        elif sub_selec=="3":
            print("Mostrando estadísticas sobre naves")
            show_stats()
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
            construir_mision()
        elif sub_selec=="2":
            print("Modificar misión")
            modificar_mision()
        elif sub_selec=="3":
            print("Visualizar misión")
            ver_mision()
        elif sub_selec=="4":
            print("Guardar misiones")
            guardar_mision()
        elif sub_selec=="5":
            print("Cargar misiones")
            cargar_mision()
        elif sub_selec=="6":
            print("Regresando al menú principal")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo")

### Main menu
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
            print('loading data from swapi...')
            load_films_from_api()
            print("films loaded...")
            load_character_from_api()
            print("characters loaded...")
            load_planets_from_api()
            print("planets loaded...")
            load_vehicles_from_api()
            print("vehicles loaded...")
            load_starships_from_api()
            print("starships loaded...")
            load_species_from_api()
            print("species loaded...")
            print('Finished loading all apis, starting application...')
            submenu()
        elif selec== "2":
            load_characters_from_csv()
            load_weapons_from_csv()
            load_planets_from_csv()
            load_starships_from_csv()
            statistics_submenu()
        elif selec=="3":
            load_characters_from_csv()
            load_weapons_from_csv()
            load_planets_from_csv()
            load_starships_from_csv()
            missions_submenu()
        elif selec=="4":
            print("Gracias por usar Star Wars Wikis. Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo")

main()









        
         
         