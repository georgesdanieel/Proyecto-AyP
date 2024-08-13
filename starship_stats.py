import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def caracteristicas_naves(starship_list):

    data = {
        "Name": [],
        "Length": [],
        "Cargo Capacity": [],
        "Hyperdrive Rating": [],
        "MGLT": []
    }
    for starship in starship_list:
        data["Name"].append(starship.name)
        data["Length"].append(float(starship.length) if starship.length else 0)
        data["Cargo Capacity"].append(float(starship.cargo_capacity) if starship.cargo_capacity else 0)
        data["Hyperdrive Rating"].append(float(starship.hyperdrive_rating) if starship.hyperdrive_rating else 0)
        data["MGLT"].append(float(starship.MGLT) if starship.MGLT else 0)
        
    df = pd.DataFrame(data) #otra forma de recolectar la info para hacer un grafico
    fig, axs = plt.subplots(2, 2, figsize=(14, 10)) 
    
 # Length Plot
    axs[0, 0].bar(df["Name"], df["Length"], color='skyblue')
    axs[0, 0].set_title('Longitud de las Naves')
    axs[0, 0].set_xlabel('Nave')
    axs[0, 0].set_ylabel('Longitud')
    axs[0, 0].tick_params(axis='x', rotation=90)

    # Cargo Capacity Plot
    axs[0, 1].bar(df["Name"], df["Cargo Capacity"], color='salmon')
    axs[0, 1].set_title('Capacidad de Carga de las Naves')
    axs[0, 1].set_xlabel('Nave')
    axs[0, 1].set_ylabel('Capacidad de Carga')
    axs[0, 1].tick_params(axis='x', rotation=90)

    # Hyperdrive Rating Plot
    axs[1, 0].bar(df["Name"], df["Hyperdrive Rating"], color='lightgreen')
    axs[1, 0].set_title('Clasificación de Hiperimpulsor de las Naves')
    axs[1, 0].set_xlabel('Nave')
    axs[1, 0].set_ylabel('Clasificación de Hiperimpulsor')
    axs[1, 0].tick_params(axis='x', rotation=90)

    # MGLT Plot
    axs[1, 1].bar(df["Name"], df["MGLT"], color='purple')
    axs[1, 1].set_title('MGLT de las Naves')
    axs[1, 1].set_xlabel('Nave')
    axs[1, 1].set_ylabel('MGLT')
    axs[1, 1].tick_params(axis='x', rotation=90)

    plt.tight_layout()
    plt.show()
    

    plt.tight_layout()
    plt.show()

