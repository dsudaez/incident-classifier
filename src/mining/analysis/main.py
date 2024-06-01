import pandas as pd
from src.mining.analysis.analyzer import Analyzer

def analyze(df, column, verbose=False):
    analyzer = Analyzer(df);
    analyzer.analyze(column);