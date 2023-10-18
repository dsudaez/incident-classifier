import pandas as pd
import numpy as np

def raise_categorias(row):
    categorias = row['DESCRIPCION']
    if (row['NUMERO_CLASIFICADOR'] == 'B.25'):
        label = 1
    else:
        label = 0
    return label

df_balanceado = pd.read_csv("C:/Users/deb/Documents/Tesis/incident-classifier/data/df_balanceado.csv")
df_balanceado['etiqueta'] = df_balanceado.apply(raise_categorias, axis=1)


del df_balanceado['FECHA_RECEPCION']
del df_balanceado['NUMERO_CLASIFICADOR']
del df_balanceado['ID_CODIGO']
del df_balanceado['DESCRIPCION']
del df_balanceado['CALLE']

ruta_destino = "C:/Users/deb/Documents/Tesis/incident-classifier/data/df_etiquetado.csv"
df_balanceado.to_csv(ruta_destino, index=False)