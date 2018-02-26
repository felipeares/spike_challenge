# Respuesta 02

Consolida los dos datasets en uno solo y genera una marca para las canciones que sean
reggaeton en base a los datasets. Entregable: csv con dataset y código (si es que usaste).

## Construcción del archivo

En el archivo [output.csv](https://github.com/felipeares/spike_challenge/tree/master/answer_02/output.csv) se puede ver el consolidado de ambos dataset, incluida una nueva columna llamada es_reggaeton. 

La construcción se realizó en Python con las librerías Pandas y NumPy. Se entiende que por el volumen menor de los datos se pudo haber realizado en mucho menos tiempo en excel, pero la idea es construir un algoritmo que funcione independiente del tamaño de los archivos.

Se aprovechó además de eliminar la columna de time_signature y quitar las filas NA

El código que arma el output.csv se puede encontrar en [merge.py](https://github.com/felipeares/spike_challenge/tree/master/answer_02/merge.py)