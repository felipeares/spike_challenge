# Importar librerías a utilizar
import json
import pandas as pd

# Cargar la tabla preparada en la pregunta anterior
output_csv = pd.read_csv('../answer_02/output.csv')

# Eliminar la primera columna y la de id_new
output_csv = output_csv.drop('id_new', 1)
output_csv = output_csv.drop('Unnamed: 0', 1)

# Pasar categóricas a dummies. En este caso sólo 'key' por que 'mode' ya vive
# en ceros y unos
output_csv = pd.concat([output_csv, pd.get_dummies(output_csv['key'], prefix='key_', drop_first = True)], axis=1)
output_csv = output_csv.drop('key', 1)

# Crear json que guardará medias y desviaciones para normailzar a modo de
# reutilizar en modelos en producción
normalization = {}
normalization['mean'] = output_csv.describe().loc['mean'].to_dict()
normalization['std'] = output_csv.describe().loc['std'].to_dict()
with open('./normalization.json', 'w') as outfile:
    json.dump(normalization, outfile)


# Normalizar la Matriz
for column in output_csv:
    if column != 'es_reggaeton':
        output_csv[column] = (output_csv[column] - normalization['mean'][column])/normalization['std'][column]

# Llevar la columna de predicción es_reggaeton al final
es_reggaeton = output_csv['es_reggaeton']
output_csv = output_csv.drop('es_reggaeton', 1) 
output_csv['es_reggaeton'] = es_reggaeton

# Guardar dataframe para ser utilizado por el archivo models.py
output_csv.to_csv('./output_dataset.csv', index = False)