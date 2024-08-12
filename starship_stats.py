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
            clase_longitud=df.groupby('starship_class')['length'].mean()
            plt.barh(clase_longitud.index, clase_longitud.values, color='green')
            plt.xticks(range(0,20000,1000))
            plt.ylabel('Clase de nave')
            plt.xlabel('Longitud')
            plt.title('Comparacion de la longitud por nave')

        elif opcion_seleccionada=='2':
            clase_cargo=df.groupby('starship_class')['cargo_capacity'].mean()
            plt.barh(clase_cargo.index, clase_cargo.values, color='green')
            plt.xticks(range(0,100000000,100000))
            plt.ylabel('Clase de nave')
            plt.xlabel('Capacidad de carga')
            plt.title('Comparacion de la capacidad de carga por nave')

        elif opcion_seleccionada=='3':
            clase_hiperimpulsor=df.groupby('starship_class')['hyperdrive_rating'].mean()
            plt.barh(clase_hiperimpulsor.index, clase_hiperimpulsor.values, color='purple')
            plt.xticks(range(0,10,1))
            plt.ylabel('Clase de nave')
            plt.xlabel('Hiperimpulsor')
            plt.title('Comparacion del hiperimpulsor por nave')
            
        elif opcion_seleccionada=='4':
            clase_mglt=df.groupby('starship_class')['MGLT'].mean()
            plt.barh(clase_mglt.index, clase_mglt.values, color='orange')
            plt.xticks(range(0,150,10))
            plt.ylabel('Clase de nave')
            plt.xlabel('MGLT')
            plt.title('Comparacion de MGLT por nave')

