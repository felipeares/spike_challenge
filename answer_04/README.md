# Respuesta 04

Evalúa tu modelo. ¿Qué performance tiene? ¿Qué métricas usas para evaluar esa
performance? ¿Por qué elegiste ese algoritmo en particular? ¿Cómo podrías mejorar la
performance ? Entregable: texto/imágenes.

## Evaluación general

En la pregunta anterior se construyeron 8 modelos de clasificación (Todos evaluados con distintos seeds de partición de set de entrenamiento y prueba). Sacando el promedio de las matrices de confusión para cada modelo (Tabla generada con las matrices de confusión en [matrices_confusion.csv](https://github.com/felipeares/spike_challenge/tree/master/answer_03/matrices_confusion.csv))

| Modelo        | Positivos OK  | Falsos Positivos | Falsos Negativos | Negativos OK | Falsas Predic.|
|---------------|---------------|------------------|------------------|--------------|---------------|
|Random Forest  |         666	|17	               |0	              |4	         |18             |                
|Red Neuronal   |         660	|15	               |6	              |6	         |22             | 
|Kernel SVM     |         666	|22	               |0	              |0	         |22             |
|Regresión Log  |         664	|20	               |2	              |2	         |22             |
|SVC            |         666	|22	               |0	              |0	         |22             |
|Árbol de Dec.  |         656	|12	               |10	              |10	         |22             |
|KNN            |         664	|20	               |3	              |2	         |23             |
|Naive Bayes    |         524	|4	               |142	              |18	         |146            |


Selecionaremos entonces como modelo final el Random Forest debido a que obtuvo el menor número de falsas predicciones.

## Archivo

La creación de estás métricas y tablas de comparación se puede ver en el archivo [models.py](https://github.com/felipeares/spike_challenge/tree/master/answer_03/models.py)


## Mejoras

...