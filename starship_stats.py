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
    df = pd.DataFrame(data)
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    axs[0, 0].bar(df["Name"], df["Length"], color='blue')
    axs[0, 0].set_title('Longitud de las Naves')
    axs[0, 0].set_xlabel('Nave')
    axs[0, 0].set_ylabel('Longitud')
    axs[0, 0].set_yticks(np.arange(0, df["Length"].max(), 100)) #me permite organizar los valores de menor a mayor
    axs[0, 0].tick_params(axis='x', rotation=90) #hace que los nombres se vean en vertical

    axs[0, 1].bar(df["Name"], df["Cargo Capacity"], color='red')
    axs[0, 1].set_title('Capacidad de Carga de las Naves')
    axs[0, 1].set_xlabel('Nave')
    axs[0, 1].set_ylabel('Capacidad de Carga por nave')
    axs[0, 1].set_yticks(np.arange(0, df["Cargo Capacity"].max(), 1000))
    axs[0, 1].tick_params(axis='x', rotation=90)

    axs[1, 0].bar(df["Name"], df["Hyperdrive Rating"], color='green')
    axs[1, 0].set_title('Clasificación de Hiperimpulsor de las Naves')
    axs[1, 0].set_xlabel('Nave')
    axs[1, 0].set_ylabel('Clasificación de Hiperimpulsor por nave')
    axs[1, 0].set_yticks(np.arange(0, df["Hyperdrive Rating"].max(), 0.5))
    axs[1, 0].tick_params(axis='x', rotation=90)

    axs[1, 1].bar(df["Name"], df["MGLT"], color='purple')
    axs[1, 1].set_title('MGLT de las Naves')
    axs[1, 1].set_xlabel('Nave')
    axs[1, 1].set_ylabel('MGLT')
    axs[1, 1].set_yticks(np.arange(0, df["MGLT"].max(), 10))
    axs[1, 1].tick_params(axis='x', rotation=90)

    plt.tight_layout()
    plt.show()

