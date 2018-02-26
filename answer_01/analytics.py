# Importar librerí­as a utilizar
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Cargar Tablas
data_todotipo = pd.read_csv('../data/data_todotipo.csv')
data_reggaeton = pd.read_csv('../data/data_reggaeton.csv')

# En caso de ser categórica devuelve el número de clases encontradas
def obtenerDescriptores(arr, bns=100, categorizar=False):    
    if categorizar:
        labelencoder = LabelEncoder()
        arr = labelencoder.fit_transform(arr) 
        bns = len(labelencoder.classes_)
    
    arr = arr.astype(float)    
    arr = arr[~np.isnan(arr)]
    histo, bins = np.histogram(arr, bins=bns)
    plt.hist(arr, bins)
    plt.show()
    
    if categorizar:
        print('NÂº Clases ' + str(round(np.max(arr),0)+1))
        print('Media ' + str(round(np.mean(histo),2)))
        print('Min ' + str(round(np.min(histo),2)))
        print('Max ' + str(round(np.max(histo),2)))
        print('Desv ' + str(round(np.std(histo),2)))

# Mirada general del archivo data_todotipo.csv
data_todotipo_describe = data_todotipo.describe()
data_todotipo_describe.to_csv('./tables/data_todotipo_describe.csv', index = False)

# Mirada general del archivo data_todotipo.csv
data_reggaeton_describe = data_reggaeton.describe()
data_reggaeton_describe.to_csv('./tables/data_reggaeton_describe.csv', index = False)

# Miradas por variable. Pasar primero a Matriz NumPy
data_todotipo_numpy = data_todotipo.values
data_reggaeton_numpy = data_reggaeton.values

# Graficar distribuciones data_todotipo_numpy
obtenerDescriptores(data_todotipo_numpy[:,1])
obtenerDescriptores(data_todotipo_numpy[:,2])
obtenerDescriptores(data_todotipo_numpy[:,3])
obtenerDescriptores(data_todotipo_numpy[:,4])
obtenerDescriptores(data_todotipo_numpy[:,5])
obtenerDescriptores(data_todotipo_numpy[:,6])
obtenerDescriptores(data_todotipo_numpy[:,7])
obtenerDescriptores(data_todotipo_numpy[:,8])
obtenerDescriptores(data_todotipo_numpy[:,9])
obtenerDescriptores(data_todotipo_numpy[:,10])
obtenerDescriptores(data_todotipo_numpy[:,11])
obtenerDescriptores(data_todotipo_numpy[:,12])
obtenerDescriptores(data_todotipo_numpy[:,13])
obtenerDescriptores(data_todotipo_numpy[:,14])

# Graficar distribuciones data_reggaeton_numpy
obtenerDescriptores(data_reggaeton_numpy[:,1])
obtenerDescriptores(data_reggaeton_numpy[:,2])
obtenerDescriptores(data_reggaeton_numpy[:,3])
obtenerDescriptores(data_reggaeton_numpy[:,4])
obtenerDescriptores(data_reggaeton_numpy[:,5])
obtenerDescriptores(data_reggaeton_numpy[:,6])
obtenerDescriptores(data_reggaeton_numpy[:,7])
obtenerDescriptores(data_reggaeton_numpy[:,8])
obtenerDescriptores(data_reggaeton_numpy[:,9])
obtenerDescriptores(data_reggaeton_numpy[:,10])
obtenerDescriptores(data_reggaeton_numpy[:,11])
obtenerDescriptores(data_reggaeton_numpy[:,12])
obtenerDescriptores(data_reggaeton_numpy[:,13])
obtenerDescriptores(data_reggaeton_numpy[:,14])

