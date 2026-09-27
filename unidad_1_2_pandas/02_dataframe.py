import pandas as pd
import numpy as np
from tabulate import tabulate

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 149995} # diccionario de areas
area = pd.Series(area_dict)

states_list = ['Illinois','Texas','New York', 'Florida', 'California'] # lista de estados
states_pop = [12882135, 26448193, 19651127, 19552860, 38332521] # lista de poblaciones
population = pd.Series(states_pop, index= states_list) # series de poblaciones

states = pd.DataFrame({'population': population, 'area': area}) # dataframe de estados con las series de poblaciones y areas

# headers="keys" usa los nombres de columnas; tablefmt define el estilo de bordes
print("states:")
print(tabulate(states, headers="keys", tablefmt="psql"))

print(f"states.index: {states.index}")

print(f"states.columns: {states.columns}")

print(f"states.values: {states.values}")

print(f"states.shape: {states.shape}")

print(f"states.size: {states.size}")