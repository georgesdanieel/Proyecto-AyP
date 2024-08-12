import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def personaje_por_mundo():

    file= '/Users/valentinavizcarrondo/Documents/GitHub/Proyecto-AyP/Proyecto-AyP/Proyecto-AyP/csv/characters.csv'
    df= pd.read_csv(file)
    
    planet_counts = df['Planet'].value_counts()

    plt.figure(figsize=(10, 6))
    planet_counts.plot(kind='barh', color='red')
    plt.title('Cantidad de personajes nacidos en cada planeta')
    plt.xlabel('Planeta')
    plt.ylabel('Cantidad de personajes')
    plt.show()

def characteristicas_naves(starship_list):

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

    #Length
    axs[0, 0].bar(df["Name"], df["Length"], color='blue')
    axs[0, 0].set_title('Longitud de las Naves')
    axs[0, 0].set_xlabel('Nave')
    axs[0, 0].set_ylabel('Longitud')

    #Cargo
    axs[0, 1].bar(df["Name"], df["Cargo Capacity"], color='red')
    axs[0, 1].set_title('Capacidad de Carga de las Naves')
    axs[0, 1].set_xlabel('Nave')
    axs[0, 1].set_ylabel('Capacidad de Carga por nave')

    # Hyperdrive Rating
    axs[1, 0].bar(df["Name"], df["Hyperdrive Rating"], color='green')
    axs[1, 0].set_title('Clasificación de Hiperimpulsor de las Naves')
    axs[1, 0].set_xlabel('Nave')
    axs[1, 0].set_ylabel('Clasificación de Hiperimpulsor por nave')

    # MGLT
    axs[1, 1].bar(df["Name"], df["MGLT"], color='purple')
    axs[1, 1].set_title('MGLT de las Naves')
    axs[1, 1].set_xlabel('Nave')
    axs[1, 1].set_ylabel('MGLT')

    plt.tight_layout()
    plt.show()

def stats_generales():
    file=('/Users/valentinavizcarrondo/Downloads/Proyecto-AyP-main-2/starships.csv')
    df = pd.read_csv(file)

    parametros=['MGLT','hyperdrive_rating','cost_in_credits','max_atmosphering_speed']

    clasificacion= {}

    for parametro in parametros:
        clase=df.groupby('starship_class')[parametro].agg(['count','mean', 'max', 'min'])
        moda=df.groupby('starship_class')[parametro].agg(lambda x: x.value_counts().index[0] if len(x.value_counts()) > 0 else np.nan)
        clase['mode']=moda
        clasificacion[parametro]=clase

    opciones={

    '1':'MGLT',
    '2':'hyperdrive_rating',
    '3':'cost_in_credits',
    '4':'max_atmosphering_speed'

    }

    while True:
        print('\n Seleccione una opcion para ver sus estadisticas. Coloca cualquier letra para salir')
        for key, value in opciones.items():
            print(f'{key}. {value}')
        opcion_seleccionada=input('--->  ')

        if opcion_seleccionada=='1':
            print('Estadisticas de los tipos de naves segun MGLT')
            print(clasificacion['MGLT'])
        elif opcion_seleccionada=='2':
            print('Estadisticas de los tipos de naves segun hiperimpulsor')
            print(clasificacion['hyperdrive_rating'])
        elif opcion_seleccionada=='3':
            print('Estadisticas de los tipos de naves segun su costo')
            print(clasificacion['cost_in_credits'])
        elif opcion_seleccionada=='4':
            print('Estadisticas de los tipos de naves segun su maxima velocidad atmósferico')
            print(clasificacion['max_atmosphering_speed'])
        else:
            print('Has salido con exito')
            break
