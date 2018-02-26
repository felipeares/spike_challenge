# Importar librerías a utilizar
import json
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from keras.models import load_model

# Cargar el modelo Random Forest
random_forest = joblib.load('../answer_03/saved_models/modelo_RF.pkl') 

# Cargar la red neuronal
neural_net = load_model('../answer_03/saved_models/modelo_RNA.pkl')

# Cargar el dataset de prueba
data_test = pd.read_csv('../data/data_test.csv')

# Guardar el dataset en otra variable para trabajar
data_test_matrix = data_test

# Eliminar la primera columna y la de id_new
data_test_matrix = data_test_matrix.drop('id_new', 1)
data_test_matrix = data_test_matrix.drop('Unnamed: 0', 1)
data_test_matrix = data_test_matrix.drop('time_signature', 1)

# Pasar categóricas a dummies. En este caso sólo 'key' por que 'mode' ya vive
# en ceros y unos
data_test_matrix['key'] = data_test_matrix['key'].astype('float')
data_test_matrix = pd.concat([data_test_matrix, 
                              pd.get_dummies(data_test_matrix['key'], 
                                             prefix='key_', 
                                             drop_first = True)], axis=1)
data_test_matrix = data_test_matrix.drop('key', 1)

# Agregar columnas que falten
data_test_matrix.insert(loc=14, column='key__3.0', value=0)

# Cargar el archivo de normailización y normalizar
normalization = json.load(open('../answer_03/normalization.json'))

# Normalizar la Matriz
for column in data_test_matrix:
    data_test_matrix[column] = (data_test_matrix[column] - normalization['mean'][column])/normalization['std'][column]

# Transformar a matriz
X = data_test_matrix.iloc[:, :].values

# Predecir reggaetones
y_pred = random_forest.predict(X)

# Calcular probabilidad
y_prob = neural_net.predict(X)

# Agrgar columnas a la matriz original
data_test['es_reggaeton'] = y_pred
data_test['prob_reggaeton'] = y_prob

# Guardar output
data_test.to_csv('./output_final.csv', index = False)
