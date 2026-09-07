from dictionary import Dictionary

class Translator:

    def __init__(self, dict = Dictionary()):
        self.dict = dict

    def printMenu(self):
        print("-----------------------------\n"
              "Translator Alien-Italian\n"
              "-----------------------------\n"
              "1. Aggiungi nuova parola\n"
              "2. Cerca una traduzione\n"
              "3. Cerca con wildcard\n"
              "4. Stampa il dizionario\n"
              "5. Exit\n"
              "-----------------------------\n")

    def loadDictionary(self, dict):
        self.dict.loadDictionary()

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.dict.addWord(entry)

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        self.dict.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        self.dict.translateWordWildCard(query)

    def handlePrint(self):
        self.dict.print()
