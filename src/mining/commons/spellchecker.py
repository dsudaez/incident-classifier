import numpy as np
from spellchecker import SpellChecker

class SpellCheck:
    spell = {}

    def __init__(self):
        self.spell = SpellChecker(language='es')

    def correct(self, word):
        return self.spell.correction(word)

    def candidates(self, word):
        return self.spell.candidates(word)
    
    def correct_sentence(self, value):
        words = np.array(value.split())
        fixed_words = []

        for word in words:
            fixed = self.correct(word);
            if fixed is None:
                fixed_words.append(word)
            else:
                fixed_words.append(fixed)
        final = " ".join(fixed_words)
        return final
    
    def get_fixed_words(self, value):
        words = np.array(value.split())
        fixed_words = {}

        for word in words:
            fixed = self.correct(word);
            if fixed != word:
                fixed_words[word] = fixed
       
        return fixed_words