import matplotlib.pyplot as plt
import pandas as pd

def plot_characters_per_planet(character_list):
    # Collect data
    planet_names = [character.homeworld for character in character_list]

    # Create DataFrame
    df = pd.DataFrame(planet_names, columns=['Planet'])
    
    # Count the number of characters per planet
    planet_counts = df['Planet'].value_counts()

    # Generate the plot
    plt.figure(figsize=(10, 6))
    planet_counts.plot(kind='bar', color='skyblue')
    plt.title('Cantidad de personajes nacidos en cada planeta')
    plt.xlabel('Planeta')
    plt.ylabel('Cantidad de personajes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

