
import pandas as pd
from src.mining.preprocessing.main import preprocess

def process_dataset(df, verbose=False):
    ## Preprocess
    df["PROCESADO"] = df["COMENTARIO"].apply(preprocess)
    df_to_csv = pd.DataFrame(df)
    df_to_csv.to_csv("C:/Users/deb/Documents/Tesis/incident-classifier/data/test.csv")



incidencias = pd.read_csv("C:/Users/deb/Documents/Tesis/incident-classifier/data/df_filtrado.csv")
process_dataset(incidencias)
