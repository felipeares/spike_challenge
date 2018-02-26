# Respuesta 01

Analiza los dataset data_todotipo.csv y data_reggaeton.csv . ¿Qué puedes decir de los datos,
distribuciones, missing, etc? ¿En qué se diferencian? Entregable: texto/imágenes.

## Missing Data

La tabla de data_reggaeton no presenta datos nulos. La tabla data_todotipo presenta 8 filas con datos nulos "NA", los cuales serán excluidos del análisis.

## Diferencias entre archivos

1. El archivo con reggaeton NO tiene la variable time_signature

2. A continuación se presenta una tabla comparativa entre las medias de cada archivo y sus desviaciones estándar. La columna de DIFF da cuenta de cuantas desviaciones estándar (deviaciones de la tabla data_todotipo) tiene de diferencia entre medias la variable en la tabla de data_todotipo con la de data_reggaeton. (Detalles de las distribuciones en la carpeta "tablas")

|MEAN ALL       |MEAN   |REGG	|STD ALL|STD REG|DIFF   |
|---------------|-------|-------|-------|-------|-------|
|popularity	    |51.94	|56.96	|17.64	|10.70	|-28%   |
|danceability	|0.57	|0.78	|0.17	|0.08	|-126%  |
|energy	        |0.61	|0.78	|0.28	|0.10	|-61%   |
|key	        |5.18	|5.60	|3.52	|3.70	|-12%   |
|loudness	    |-9.64	|-6.33	|6.14	|2.24	|-54%   |
|mode	        |0.60	|0.57	|0.49	|0.50	|5%     |
|speechiness	|0.07	|0.12	|0.06	|0.08	|-83%   |
|acousticness	|0.35	|0.16	|0.36	|0.13	|52%    |
|instrumentaln  |0.22	|0.01	|0.35	|0.03	|60%    |
|liveness	    |0.18	|0.19	|0.15	|0.13	|-6%    |
|valence	    |0.53	|0.70	|0.28	|0.15	|-62%   |
|tempo	        |118.34	|105.91	|28.53	|28.55	|44%    |
|duration	    |233,872|275,646|77,944	|257,543|-54%   |

3. De la tabla se concluye que existen notorias diferencias entre ambos archivos, sobre todo en variables como danceability, speechiness, valence, energy e instrumentaln.

## Distribución

Entendiendo que se podría hacer un análisis mucho más detallado de las distribuciones de las variables se presenta a continuación sólo una visualización de los histograma de cada una de ellas para el archivo data_todotipo.csv. Se pueden ver varias distribuciones en formato de "cola" y asumir que ninguna tiene una distribución normal.

![Histogramas](https://github.com/felipeares/spike_challenge/blob/master/answer_01/images/histo_data_all.png "Histogramas")