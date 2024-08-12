import matplotlib.pyplot as plt
import pandas as pd

file='/Users/valentinavizcarrondo/Downloads/Proyecto-AyP-main/csv/starships.csv'
df=pd.read_csv(file)

nave=df['name']
longitud=df['length']
cargo=df['cargo_capacity']
hiperimpulsor=df['']
mglt=df['MGLT']

def 

plt.figure(figsize=(14,9))
plt.barh(nave, longitud, color='green')

plt.xticks(range(0,20000,1000))
plt.ylabel('Nombre de la nave')
plt.xlabel('Longitud')

plt.title('Comparacion de la longitud de cada nave')

plt.show()

plt.figure(figsize=(14,9))
plt.barh(nave, cargo, color='blue')

plt.ylabel('Nombre de la nave')
plt.xlabel('Cargo')

plt.title('Capacidad de carga de la nave')

plt.show()



plt.figure(figsize=(14,9))

plt.barh(nave, mglt, color='purple')
plt.xticks(range(0,150,10))

plt.ylabel('Nombre de la nave')
plt.xlabel('MGLT')

plt.title('MGLT por nave')

plt.show()