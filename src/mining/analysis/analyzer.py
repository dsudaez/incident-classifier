import pandas as pd
import multiprocessing as mp
from src.mining.commons.spellchecker import SpellCheck
from src.mining.commons.helpers import df_tocsv
import matplotlib.pyplot as plt


class Analyzer:
    dataframe = {}

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.spellchecker = SpellCheck()
    
    def analyze(self, column):
        self.empty_lines(column)
        #self.grammar_check(column)

    def empty_lines(self, column):
       # Crear una máscara booleana para identificar las filas vacías en la columna
        filas_vacias = self.dataframe[column].isna()

        # Contar el número de filas vacías y no vacías en la columna
        num_filas_vacias = filas_vacias.sum()
        num_filas_no_vacias = len(self.dataframe) - num_filas_vacias

        # Crear un DataFrame con los resultados
        resultados = pd.DataFrame({'Estado': ['Vacías', 'No Vacías'],
                                'Cantidad': [num_filas_vacias, num_filas_no_vacias]})
        # Crear una lista de colores personalizados (por ejemplo, azul y verde)
        colores = ['blue', 'green']

        # Grosor de las líneas
        linewidth = 5.0

        # Imprimir el DataFrame con los resultados
        print(resultados)

        # Crear un gráfico de torta
        plt.figure(figsize=(4, 4))
        plt.pie(resultados['Cantidad'], labels=resultados['Estado'], autopct='%1.3f%%', startangle=0, colors=colores, wedgeprops={'linewidth': linewidth})
        plt.title(f'Distribución de filas en la columna "{column}"')
        plt.axis('equal')  # Para asegurarse de que el gráfico sea circular

        # Mostrar el gráfico
        plt.show()
    
    def grammar_check(self, column):
        senteces_check = pd.DataFrame()  
        p = mp.Pool(mp.cpu_count()) # Data parallelism Object
        senteces_check['original'] = self.dataframe[column]
        senteces_check['fixed']  = p.map(self.spellchecker.correct_sentence, self.dataframe[column])

        word_check = pd.DataFrame()  
        word_check['fixed']  = p.map(self.spellchecker.get_fixed_words, self.dataframe[column])

        df_tocsv(senteces_check, 'grammar_senteces_check', 'analysis')
        df_tocsv(word_check, 'grammar_word_check', 'analysis')