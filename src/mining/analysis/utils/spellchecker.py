from spellchecker import SpellChecker

class SpellChecker:
    spell = {}

    def __init__(self):
        self.spell = SpellChecker(language='es')

    def correct(self, word):
        return self.spell.correction(word)

    def candidates(self, word):
        return self.spell.candidates(word)
        