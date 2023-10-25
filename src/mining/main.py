
import pandas as pd
from src.mining.preprocessing.main import preprocess

def process_dataset(df, verbose=False):
    ## Preprocess
    df["tokens"] = df["COMENTARIO"].apply(preprocess)
    print(df)



incidencias = pd.read_csv("C:/Users/deb/Documents/Tesis/incident-classifier/data/df_filtrado.csv")
process_dataset(incidencias)
