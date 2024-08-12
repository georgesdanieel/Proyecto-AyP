import matplotlib.pyplot as plt
import pandas as pd

file= '/Users/valentinavizcarrondo/Downloads/Proyecto-AyP-main/csv/planets.csv'
df= pd.read_csv(file)

planets=df['name']
characters = []

for resident in df['residents']:
    characters.append(len(resident.split(','))) #cambiar a algo mas creible

plt.barh(planets,characters, color='red') #quiero q se me separe cada 1 unidad

plt.xticks(range(0,5,1))
plt.xlabel('Número de personajes')
plt.ylabel('Planetas')

plt.title('Número de personajes por planeta')

plt.show()

