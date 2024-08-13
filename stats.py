import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file=('/Users/valentinavizcarrondo/Documents/GitHub/Proyecto-AyP/Proyecto-AyP/Proyecto-AyP/csv/starships.csv')
df = pd.read_csv(file)

parametros=['MGLT','hyperdrive_rating','cost_in_credits','max_atmosphering_speed']

clasificacion= {}

for parametro in parametros:
    clase=df.groupby('starship_class')[parametro].agg(['count','mean', 'max', 'min']) #groupby me permite agregar por clase
    moda=df.groupby('starship_class')[parametro].agg(lambda x: x.value_counts().index[0] if len(x.value_counts()) > 0 else np.nan)
    clase['mode']=moda
    clasificacion[parametro]=clase
    
def stats_generales():
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
