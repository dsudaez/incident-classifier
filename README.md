# Incident Classifier
Incident classifier for 911 monitoring center at Jujuy

## Estructura del proyecto
- src/app: 
Contiene la logica de la aplicación en donde se podra testear el clasificador.
- src/mining
Contiene el código implicado en cada etapa de Text Mining: preprocesamiento, modelado, analizador de los datos, etc.

## Levantar el proyecto Localmente
### Prerequisitos
- Tener instalado Python 3
- Tener instalado pip

### Paso a paso
1) Para empezar a correr el proyecto primero se debe crear un entorno virtual usando venv, debido a que es mejor tener nuestro proyecto aislado de la version principal de python que maneja la maquina. 
Se puede seguir el siguiente tutorial: https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python

2) Una vez creado el entorno virtual se debe activarlo 
    ```sh
    env/Scripts/activate.bat //In CMD para windows
    env/Scripts/Activate.ps1 //In Powershel para windows
    ```
3) Instalar todas las dependencias que se encuentran en requirements.txt (asegurar de estar en el entorno virtual)
    ```sh
   pip install -r requirements.txt
    ```
4) Para levantar la App correr el archivo app.py o desde el vscode
    ```sh
    python app.py
    ```
5) Para correr algun paso de preprocesamiento, se debe correr el main.py de cada directorio. (EN CONSTRUCCION)
    ```sh
    python ../mining/preprocessing/main.py // El path al archivo de cada main.py.
    ```

## License

MIT


