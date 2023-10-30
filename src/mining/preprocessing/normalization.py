import re
import unicodedata
from src.mining.preprocessing.utils.abbreviations import abbreviations

class Normalization:

    #Main function
    def normalize(self, incid):
        if isinstance(incid, str):
            incid = self.minus(incid)
            #incid = self.check_spell(incid)
            incid = self.remove_punctuation_accents_and_numbers(incid)
            incid = self.convert_abbreviations(incid)
            incid = self.word_repetition(incid)
        else:
            print("error")
        return incid
    
    # Función para corregir ortografía en español
    def check_spell(self, incid):
        # palabras = incid.split()

        # for i, palabra in enumerate(palabras):
        #     palabra_corregida = spell.correction(palabra)
        #     palabras[i] = palabra_corregida

        #     texto_corregido = " ".join(palabras)
        return incid
            
    # Función para convertir a minúsculas
    def minus(self, incid):
        incid = incid.lower()
        return incid
    
    # Funcion para reemplazar la repetición de letras
    def word_repetition(self, incid):
        #reemplazar la repetición de letras (excepto 'rr', 'll', 'nn') con una sola aparición
        incid = re.sub(r'((?!o|r|l)(.)\2+)', r'\2', incid)
        # Reemplazar la repetición de 'rr', 'll', 'nn' con una sola aparición
        incid = re.sub(r'(rr|ll)\1+', r'\1\1', incid)
        return incid
    
    # Función para remover acentos y numeros
    def remove_punctuation_accents_and_numbers(self, incid, default_replace=""):
        #unicodedata para eliminar acentos y la función re.sub() para eliminar los signos de puntuación.
        # Eliminar acentos
        incid = unicodedata.normalize('NFKD', incid).encode('ASCII', 'ignore').decode('utf-8')

        # Eliminar signos de puntuación
        incid = re.sub(r'[^\w\s]', default_replace, incid)
        incid = re.sub(r'\d', default_replace, incid)

        return incid

    #Funcion que convierte las abreviaturas a su forma original
    def convert_abbreviations(self, incid):
        words = incid.split()  # Dividir el texto en palabras
        words_converted = []
        for word in words:
            # Verificar si la palabra es una abreviatura y convertirla si es necesario
            word_converted = abbreviations.get(word, word)
            words_converted.append(word_converted)

        return " ".join(words_converted)  # Reunir las palabras convertidas en una cadena