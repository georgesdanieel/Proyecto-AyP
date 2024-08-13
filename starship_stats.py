import matplotlib.pyplot as plt
import pandas as pd

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
        data["Length"].append(starship.length)
        data["Cargo Capacity"].append(starship.cargo_capacity)
        data["Hyperdrive Rating"].append(starship.hyperdrive_rating)
        data["MGLT"].append(starship.MGLT)

    df = pd.DataFrame(data)
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    axs[0, 0].bar(df["Name"], df["Length"], color='blue')
    axs[0, 0].set_title('Longitud de las Naves')
    axs[0, 0].set_xlabel('Nave')
    axs[0, 0].set_ylabel('Longitud')
    axs[0, 0].tick_params(axis='x', rotation=90)

    axs[0, 1].bar(df["Name"], df["Cargo Capacity"], color='red')
    axs[0, 1].set_title('Capacidad de Carga de las Naves')
    axs[0, 1].set_xlabel('Nave')
    axs[0, 1].set_ylabel('Capacidad de Carga por nave')
    axs[0, 1].tick_params(axis='x', rotation=90)

    axs[1, 0].bar(df["Name"], df["Hyperdrive Rating"], color='green')
    axs[1, 0].set_title('Clasificación de Hiperimpulsor de las Naves')
    axs[1, 0].set_xlabel('Nave')
    axs[1, 0].set_ylabel('Clasificación de Hiperimpulsor por nave')
    axs[1, 0].tick_params(axis='x', rotation=90)

    axs[1, 1].bar(df["Name"], df["MGLT"], color='purple')
    axs[1, 1].set_title('MGLT de las Naves')
    axs[1, 1].set_xlabel('Nave')
    axs[1, 1].set_ylabel('MGLT')
    axs[1, 1].tick_params(axis='x', rotation=90)

    plt.tight_layout()
    plt.show()

