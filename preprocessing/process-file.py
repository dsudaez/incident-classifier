import pandas as pd
import numpy as np

def raise_categorias(row):
    categorias = row['DESCRIPCION']
    if (row['NUMERO_CLASIFICADOR'] == 'B.25') or (row['NUMERO_CLASIFICADOR'] == 'B.27') or (row['NUMERO_CLASIFICADOR'] == 'B.28'):
        label = 'yes'
    else:
        label = 'no'
    return label

df_incidencias = pd.read_csv("C:/Users/deb/Documents/Tesis/incident-classifier/data/df_filtrado.csv")
df_incidencias['etiqueta'] = df_incidencias.apply(raise_categorias, axis=1)


del df_incidencias['FECHA_RECEPCION']
del df_incidencias['NUMERO_CLASIFICADOR']
del df_incidencias['ID_CODIGO']
del df_incidencias['DESCRIPCION']

ruta_destino = "C:/Users/deb/Documents/Tesis/incident-classifier/data/df_etiquetado.csv"
df_incidencias.to_csv(ruta_destino, index=False)