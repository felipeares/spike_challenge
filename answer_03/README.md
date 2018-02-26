# Respuesta 03

Entrena uno o varios modelos (usando el/los algoritmo(s) que prefieras) para detectar qué
canciones son reggaeton. Entregable: modelo en cualquier formato y código (si es que
usaste).

## Construcción de Modelos

Se probaron 8 modelos de clasificación utilizando la librería SciKit y Keras (Red neuronal). Antes de construir el modelo se prepararon los datos (normalización, limpieza de variables nulas y traspaso de variables descriptivas a dummies). Los distintos modelos se pueden encontrar en la carpeta [saved_models](https://github.com/felipeares/spike_challenge/tree/master/answer_03/saved_models). El código de limpieza es [clean.py](https://github.com/felipeares/spike_challenge/tree/master/answer_03/clean.py) y el de construcción de modelos es [models.py](https://github.com/felipeares/spike_challenge/tree/master/answer_03/models.py)

### Modelos:
1. Regressión Logística
2. KNN
3. SVC
4. Naive Bayes
5. Arbol de Decisión (Clasificador)
6. Random Forest (Clasificador)
7. Kernel SVM (Con transformación)
8. Red Neuronal Densa con capa intermedia

## Limpieza

Se normalizaron todas las variables (excepto la variable de predicción) y se pasó a dummie la variable 'key'. Los parámetros de normalización de cada variable (Media y Desviación) se guardaron el archivo de [normalization.json](https://github.com/felipeares/spike_challenge/tree/master/answer_03/normalization.json)