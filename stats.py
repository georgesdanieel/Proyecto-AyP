import matplotlib.pyplot as plt
import pandas as pd

def plot_characters_per_planet(character_list):
   
    for character in character_list:
        planet_names = character.homeworld
   
    df = pd.DataFrame(planet_names, columns=['Planet'])
    
    planet_counts = df['Planet'].value_counts()

    plt.figure(figsize=(10, 6))
    planet_counts.plot(kind='bar', color='red')
    plt.title('Cantidad de personajes nacidos en cada planeta')
    plt.xlabel('Planeta')
    plt.ylabel('Cantidad de personajes')
    plt.show()

def plot_starship_characteristics(starship_list):

    data = {
        "Name": [],
        "Length": [],
        "Cargo Capacity": [],
        "Hyperdrive Rating": [],
        "MGLT": []
    }
    for starship in starship_list:
        data["Name"].append(starship.name)
        data["Length"].append(float(starship.length))
        data["Cargo Capacity"].append(float(starship.cargo_capacity))
        data["Hyperdrive Rating"].append(float(starship.hyperdrive_rating))
        data["MGLT"].append(float(starship.MGLT))

    df = pd.DataFrame(data)
    
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
