import time

from multiDictionary import MultiDictionary

class SpellChecker:

    def __init__(self, md = MultiDictionary()):
        self.md = md

    def handleSentence(self, txtIn, language):
        language = f'{language}.txt'
        txtIn = replaceChars(txtIn)
        words = txtIn.split(" ")
        self.md.searchWord(words, language)


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text.lower()