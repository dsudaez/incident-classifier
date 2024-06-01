import os
import pandas as pd

def process_files():
    combined = create_dataset()
    no_duplicated = delete_duplicated()
    deleted_rows = combined.shape[0] - no_duplicated.shape[0]


    print('###############')
    print('####### INFO ########')
    print('TOTAL ROWS:', combined.shape[0])
    print('TOTAL ROWS NO DUPLICATED:', no_duplicated.shape[0])    
    print('ROWS DELETED:', deleted_rows)

    check_gender_classification()

    print('######## END #######')


def create_dataset():
    carpeta = './data'
    dfs = []

    try: 
        for file in os.listdir(carpeta):
            if file.endswith('.csv'):  # Solo procesar archivos CSV
                location = os.path.join(carpeta, file)
                df = pd.read_csv(location, engine='python')
                dfs.append(df)

        combined_df = pd.concat(dfs, ignore_index=True)
        combined_df.to_csv('combined_data.csv', index=False)

        return combined_df
    except Exception as e:
        print(e)

def delete_duplicated():
    try:
        df = pd.read_csv('combined_data.csv', engine='python')

        combined_df_no_duplicates = df.drop_duplicates(subset=['COMENTARIO'])
        combined_df_no_duplicates.to_csv("combined_data_no_duplicates.csv", index=False)

        return combined_df_no_duplicates
    except Exception as e:
        print(e)

def check_gender_classification():
    try:
        df = pd.read_csv('combined_data_no_duplicates.csv', engine='python')
        # filtered_numeros_clasificadores = df[(df['VG'] != 0) & (df['VG'] != 1)]['NUMERO_CLASIFICADOR']
        # print(len(filtered_numeros_clasificadores))

        # print("WRONG CLASSIFICATIONS?")
        # print('NO' if filtered_numeros_clasificadores.empty else filtered_numeros_clasificadores)

        violence_gender = df['VG'].value_counts()
        print('RESUME OF CLASSIFICATION:')
        print(violence_gender)
    except Exception as e:
        print(e)

## MAIN
process_files()
