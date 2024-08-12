import matplotlib.pyplot as plt
import pandas as pd

file='/Users/valentinavizcarrondo/Downloads/Proyecto-AyP-main/csv/starships.csv'
df=pd.read_csv(file)

longitud=df['length']
cargo=df['cargo_capacity']
hiperimpulsor=df['hyperdrive_rating']
mglt=df['MGLT']
clase=df.groupby('starship_class')

def spaceship_graphs():
    menu={
        '1':'Longitud',
        '2':'Capacidad de carga',
        '3':'Hiperimpulsor',
        '4':'MGLT'
}
    while True:
        print('\n Seleccione una opcion para ver sus estadisticas. Coloca cualquier letra para salir')
        for key, value in menu.items():
            print(f'{key}- {value}')
        opcion_seleccionada=input('--->  ')
        if opcion_seleccionada=='1':
            plt.figure(figsize=(14,9))
            plt.barh(clase, longitud, color='green')

            plt.xticks(range(0,20000,1000))
            plt.ylabel('Nombre de la nave')
            plt.xlabel('Longitud')
            plt.title('Comparacion de la longitud de cada nave')

spaceship_graphs()


