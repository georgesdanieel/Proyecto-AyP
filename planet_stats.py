import matplotlib.pyplot as plt
import pandas as pd

file= '/Users/valentinavizcarrondo/Documents/GitHub/Proyecto-AyP/Proyecto-AyP/Proyecto-AyP/csv/characters.csv'
df= pd.read_csv(file)

planets=df['homeworld'].value_counts().index
characters =df['homeworld'].value_counts().values

plt.barh(range(len(planets)),characters, color='red') #quiero q se me separe cada 1 unidad
plt.yticks(range(len(planets)), planets)

plt.xlabel('Número de personajes')
plt.ylabel('Planetas')
plt.title('Número de personajes por planeta')

plt.show()

