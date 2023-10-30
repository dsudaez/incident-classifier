import pandas as pd
from src.mining.analysis.analyzer import Analyzer

def analyze_dataset(df, verbose=False):
    analyzer = Analyzer(df)
    analyzer.grammar_check();



incidencias = pd.read_csv("C:/Users/deb/Documents/Tesis/incident-classifier/data/df_filtrado.csv")
analyze_dataset(incidencias)
