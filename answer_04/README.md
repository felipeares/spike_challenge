# Respuesta 04

Evalúa tu modelo. ¿Qué performance tiene? ¿Qué métricas usas para evaluar esa
performance? ¿Por qué elegiste ese algoritmo en particular? ¿Cómo podrías mejorar la
performance ? Entregable: texto/imágenes.

## Evaluación general

Utilizando la métrica de mínimos cuadrados sobre el dataset de prueba (data_reggaeton.csv) se compararon los distintos modelos trabajados en la pregunta anterior. Se construyeron distintos modelos con distintos parámetros para poder comparar de mejor manera el resultado. El resultado fue el siguiente:

| Modelo        | Error Promedio|
| ------------- |:-------------:|
| col 3 is      | right-aligned |
| col 2 is      | centered      |
| zebra stripes | are neat      |

Selecionaremos entonces como modelo final la regresión lineal debido a que obtuvo el menor error en mínimos cudrados.

## Archivos

Se puede revisar el código en [evaluation.py](http://www.google.com)

## Mejoras

El modelo podría mejorar incorporando ayor volumen de datos o nuevas columnas con informción adicional de las distintas canciones.