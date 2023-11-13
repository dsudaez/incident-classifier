import time
import pandas as pd
from src.mining.preprocessing.main import preprocess
from src.mining.analysis.main import analyze


def process_dataset(df, verbose=False):
    ## Preprocess
    preprocess(df, 'COMENTARIO')
    # df_to_csv = pd.DataFrame(df)
    # df_to_csv.to_csv("C:/Users/deb/Documents/Tesis/incident-classifier/data/test.csv")

def analyze_dataset(df, verbose=False):
    ## analyze
    analyze(df, 'COMENTARIO')

#### INITIAL EXECUTION
if __name__ == '__main__':    
    start_time = time.time()

    incidencias = pd.read_csv("C:/Users/deb/Documents/Tesis/incident-classifier/data/df_filtrado_short.csv")
    analyze_dataset(incidencias)

    print("--- %s seconds ---" % (time.time() - start_time))

