# Respuesta 05

Aplica tu modelo sobre el dataset “data_test.csv”, agregándole a cada registro dos nuevos
campos: marca_reggaeton (un 1 cuando es reggaetón, un 0 cuando no lo es) y
probabilidad_reggaeton (probabilidad de que la canción sea reggaeton). ¿Cómo elegiste
cuáles marcar? ¿De qué depende que predigas la existencia de mayor o menor cantidad de
reggaetones? Entregable: texto/imágenes.

## Selección

Se construyó el archivo [output_final.csv](https://github.com/felipeares/spike_challenge/tree/master/answer_05/output_final.csv) con las distintas filas y su marca (marca_reggaeton) y probabilidad (probabilidad_reggaeton). La marca_reggaeton se construyó utilizando el modelo de Random Forest seleccionado en la pregunta anterior. Este modelo arroja una clasificación por lo que para construir una variable predictora de la probabilidad de ser reggaeton (probabilidad_reggaeton) se utilizó la red neuronal antes construida.

La construcción del dataset se puede encontrar en [build.py](https://github.com/felipeares/spike_challenge/tree/master/answer_05/build.py)

## Conclusión

En esta actividad se construyó el flujo necesario desde la analítica hasta la construcción del output del set de prueba. Con mayor tiempo y dedicación habría que comenzar a mover los distintos parámetros (entendiendo mejor los datos, su distribución y correlación) para ir mejorando el modelo de predicción. El modelo encontrado está lejos de ser un buen modelo.
