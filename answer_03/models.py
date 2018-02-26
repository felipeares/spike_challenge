# Importar librerías a utilizar
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

# Cargar la tabla preparada en la pregunta anterior
output_dataset = pd.read_csv('./output_dataset.csv')

# Crear matriz de input X y vector de predicción y
X = output_dataset.iloc[:, :-1].values
y = output_dataset.iloc[:, -1].values

# Función para separar los set de entrenamiento y prueba
X_train = X_test = y_train = y_test = np.array([], np.float64)
def construirSetsEntrenamientoPruebas(tam = 0.3, seed = 0):
    global X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = tam, random_state = seed)

# Crear Dataframe para guardar resultados y comparar
resultados = pd.DataFrame(columns=['seed','modelo','params','0_0','1_0','0_1','1_1','good','bad'])

# Inicializar la primera seed para probar distintas distrinuciones
seed_test = 0

# Función para calcular el error de predicción como la suma, el promedio y 
# la desviación de las diferencias absolutas entre el valor real y la predicción
def obtenerError(y_prediccion, y_real, modelo = '', params = ''):
    global resultados
    
    cm = confusion_matrix(y_real, y_prediccion)
    
    s = pd.Series([seed_test, modelo, params, cm[0,0], cm[1,0], cm[0,1], cm[1,1], (cm[0,0] + cm[1,1]), (cm[1,0] + cm[0,1])], index=['seed','modelo','params','0_0','1_0','0_1','1_1','good','bad'])
    resultados = resultados.append(s, ignore_index=True)
    
    print(cm)
    
# (1) - Regresión Logística
def regresionLog(save = False):
    print('(1) Regresión Logística --------')
    # Entrenar el modelo
    modelo = LogisticRegression(random_state = 0)
    modelo.fit(X_train, y_train)
    
    # Obtener predicciones
    y_pred = modelo.predict(X_test)
    
    # Obtener error
    obtenerError(y_pred, y_test, modelo = 'REG')
    
    # Guardar
    if save:
        joblib.dump(modelo , './saved_models/modelo_REG.pkl') 
    
    return y_pred

# (2) - KNN
def modeloKNN(n = 5, save = False):
    print('(2) KNN --------')
    # Entrenar el modelo
    modelo = KNeighborsClassifier(n_neighbors = n, metric = 'minkowski', p = 2)
    modelo.fit(X_train, y_train.ravel())
    
    # Obtener predicciones
    y_pred = modelo.predict(X_test)
    
    # Obtener error
    obtenerError(y_pred, y_test, modelo = 'KNN', params = str(n))
    
    # Guardar
    if save:
        joblib.dump(modelo , './saved_models/modelo_KNN.pkl') 
    
    return y_pred

# (3) - SVC
def modeloSVC(save = False):
    print('(3) SVC --------')
    
    # Entrenar el modelo
    modelo = SVC(kernel = 'linear', random_state = 0)
    modelo.fit(X_train, y_train)
    
    # Obtener predicciones
    y_pred = modelo.predict(X_test)
    
    # Obtener error
    obtenerError(y_pred, y_test, modelo = 'SVC')
    
    # Guardar
    if save:
        joblib.dump(modelo , './saved_models/modelo_SVC.pkl') 
    
    return y_pred

# (4) - Naive Bayes
def modeloNaiveBayes(save = False):
    print('(4) Naive Bayes --------')
    
    # Entrenar el modelo
    modelo = GaussianNB()
    modelo.fit(X_train, y_train.ravel())
    
    # Obtener predicciones
    y_pred = modelo.predict(X_test)
    
    # Obtener error
    obtenerError(y_pred, y_test, modelo = 'NB')
    
    # Guardar
    if save:
        joblib.dump(modelo , './saved_models/modelo_NB.pkl') 
    
    return y_pred

# (5) - Tree Classification
def modeloDecisionTree(save = False):
    print('(5) Tree Classification --------')
    
    # Entrenar el modelo
    modelo = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    modelo.fit(X_train, y_train.ravel())
    
    # Obtener predicciones
    y_pred = modelo.predict(X_test)
    
    # Obtener error
    obtenerError(y_pred, y_test, modelo = 'TREE')
    
    # Guardar
    if save:
        joblib.dump(modelo , './saved_models/modelo_TREE.pkl') 
    
    return y_pred

# (6) - Random Forest
def modeloRandomForest(n = 10, save = False):
    print('(6) Random Forest --------')
    
    # Entrenar el modelo
    modelo = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    modelo.fit(X_train, y_train.ravel())
    
    # Obtener predicciones
    y_pred = modelo.predict(X_test)
    
    # Obtener error
    obtenerError(y_pred, y_test, modelo = 'RF', params = str(n))
    
    # Guardar
    if save:
        joblib.dump(modelo , './saved_models/modelo_RF.pkl') 
    
    return y_pred

# (7) - Kernel SVM
def modeloKernelSVM(save = False):
    print('(7) Kernel SVM --------')
    
    # Entrenar el modelo
    modelo = SVC(kernel = 'rbf', random_state = 0)
    modelo.fit(X_train, y_train)
    
    # Obtener predicciones
    y_pred = modelo.predict(X_test)
    
    # Obtener error
    obtenerError(y_pred, y_test, modelo = 'KNSVM')
    
    # Guardar
    if save:
        joblib.dump(modelo , './saved_models/modelo_KNSVM.pkl') 
    
    return y_pred

# (8) - RED NEURONAL
def redNeuronal(neuronas = 6, save = False):
    print('(5) RED NEURONAL --------')
    from keras.models import Sequential
    from keras.layers import Dense
    
    # Entrenar el modelo
    modelo = Sequential()
    
    # Primera capa de input
    modelo.add(Dense(neuronas, init='uniform', activation = 'relu', input_dim = 23))
    
    #modelo.add(Dense(output_dim = neuronas, init = 'uniform', activation = 'relu'))
    
    modelo.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))
    
    # Correr
    modelo.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    
    # Fitting
    modelo.fit(X_train, y_train, batch_size = 10, epochs = 100)
    
    # Obtener predicciones
    y_pred = modelo.predict(X_test)
    y_pred = (y_pred > 0.5)*1
    
    # Obtener error
    obtenerError(y_pred, y_test, modelo = 'RNA', params = str(neuronas))
    
    # Guardar
    if save:
        modelo.save('./saved_models/modelo_RNA.pkl') 
    
    return y_pred



"""
# Pruebas de parámetros varios
for i in range(1,50):
    seed_test = i
    construirSetsEntrenamientoPruebas(seed = seed_test)
    modeloKNN(n = i)
    modeloRandomForest(n = i)

y_pred = redNeuronal(16)
y_pred = redNeuronal(32)
y_pred = redNeuronal(64)
y_pred = redNeuronal(128)
"""

# PROBAR PROBAR PROBAR
for i in range(0,10):
    seed_test = i
    construirSetsEntrenamientoPruebas(seed = seed_test)
    y_pred = regresionLog()
    y_pred = modeloKNN()
    y_pred = modeloSVC()
    y_pred = modeloNaiveBayes()
    y_pred = modeloDecisionTree()
    y_pred = modeloRandomForest(n = 14)
    y_pred = modeloKernelSVM()
    y_pred = redNeuronal(64)

# Guardar modelos
seed_test = 1
construirSetsEntrenamientoPruebas(seed = seed_test)
y_pred = regresionLog(save = True)
y_pred = modeloKNN(save = True)
y_pred = modeloSVC(save = True)
y_pred = modeloNaiveBayes(save = True)
y_pred = modeloDecisionTree(save = True)
y_pred = modeloRandomForest(n = 14, save = True)
y_pred = modeloKernelSVM(save = True)
y_pred = redNeuronal(12, save = True)

# Guardar los resultados finales
resultados.to_csv('./matrices_confusion.csv', index = False)

