# Respuesta 05

Aplica tu modelo sobre el dataset “data_test.csv”, agregándole a cada registro dos nuevos
campos: marca_reggaeton (un 1 cuando es reggaetón, un 0 cuando no lo es) y
probabilidad_reggaeton (probabilidad de que la canción sea reggaeton). ¿Cómo elegiste
cuáles marcar? ¿De qué depende que predigas la existencia de mayor o menor cantidad de
reggaetones? Entregable: texto/imágenes.

## Selección

Se construyó el archivo [output_final.csv](http://www.google.com) con las distintas filas y su marca (marca_reggaeton) y probabilidad (probabilidad_reggaeton). La marca_reggaeton se construyó tomando todas aquellas probabilidades mayores a 0.5. La predicción de mayores cantidades de reggaetones dependerá exclusivamente del theeshold seleccionado (en este caso 0.5) y de la asertividad del modelo.

