import random

class Domanda(object):
    def __init__(self, testo = "", diff = None, corretta = "", opzioni = None):
        if (opzioni is None):
            opzioni = []
        self.testo = testo
        self.difficolta = diff
        self.corretta = corretta
        self.opzioni = opzioni

    def mix_opzioni(self):
        random.shuffle(self.opzioni)
        return self.opzioni

    def __str__(self):
        return f'Livello {self.difficolta}) {self.testo}'
