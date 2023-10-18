
import pandas as pd

df_incidencias = pd.read_csv("C:/Users/deb/Documents/Tesis/incident-classifier/data/dataset-original.csv")

# filtro por las categorias seleccionadas

df_filtrado = df_incidencias[(df_incidencias['NUMERO_CLASIFICADOR']=='B.25')|(df_incidencias['NUMERO_CLASIFICADOR']=='D.68')] 

print(df_filtrado)

ruta_destino = "C:/Users/deb/Documents/Tesis/incident-classifier/data/df_filtrado.csv"
df_filtrado.to_csv(ruta_destino, index=False)