import pandas as pd

def df_tocsv(df, filename, section):
    df_to_csv = pd.DataFrame(df)
    df_to_csv.to_csv(f'C:/Users/deb/Documents/Tesis/incident-classifier/data/{section}/{filename}.csv') 

