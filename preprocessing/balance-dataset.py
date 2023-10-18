
import pandas as pd

df_filtrado = pd.read_csv("C:/Users/deb/Documents/Tesis/incident-classifier/data/df_filtrado.csv")


df_groupone = df_filtrado[(df_filtrado['NUMERO_CLASIFICADOR']=='B.25')] 
df_grouptwo = df_filtrado[(df_filtrado['NUMERO_CLASIFICADOR']=='D.68')] 


frames = [df_groupone.iloc[0:2000], df_grouptwo.iloc[0:2000]]

df_balanceado = pd.concat(frames)

print(df_balanceado)

ruta_destino = "C:/Users/deb/Documents/Tesis/incident-classifier/data/df_balanceado.csv"
df_balanceado.to_csv(ruta_destino, index=False)