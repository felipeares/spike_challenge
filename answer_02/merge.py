# Importar librerías a utilizar
import numpy as np
import pandas as pd

# Cargar Tablas a mezclar
data_todotipo = pd.read_csv('../data/data_todotipo.csv')
data_reggaeton = pd.read_csv('../data/data_reggaeton.csv')

# Escribir nueva columna con un uno si es reggaeton y cero si no
data_todotipo['es_reggaeton'] = 0
data_reggaeton['es_reggaeton'] = 1

# Eliminar columna time_signature en data_todotipo
data_todotipo = data_todotipo.drop('time_signature', 1)

# Eliminar filas con NA
data_todotipo = data_todotipo[pd.notnull(data_todotipo['energy'])]

# Mezclar ambas tablas en una y guardar
merge_dataframe = pd.concat([data_todotipo,data_reggaeton])
merge_dataframe.to_csv('./output.csv', index = False)
