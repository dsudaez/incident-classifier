class analyzer:
    dataframe = {}

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def empty_lines(self, columna):
        # Crear una máscara booleana para identificar las filas vacías en la columna
        filas_vacias = self.dataframe[columna].isna()

        # Filtrar el DataFrame para obtener las filas vacías
        filas_vacias_df = self.dataframe[filas_vacias]

        # Imprimir el DataFrame con las filas vacías
        print(filas_vacias_df)

        # Contar el número de filas vacías en la columna
        num_filas_vacias = filas_vacias.sum()

        # Imprimir el número de filas vacías en la columna
        print(f"Número de filas vacías en la columna '{columna}': {num_filas_vacias}")