import re

class Dictionary:
    def __init__(self, dict={}):
        self.dict = dict

    def loadDictionary(self):
        with open ("dictionary.txt", "r") as file:
            for line in file:
                line = line.strip()
                key, value = line.split(" ")[0], line.split(" ")[1:]
                self.dict[str(key)] = value

    def addWord(self, entry):
        key = str(entry.split(" ")[0])
        values = entry.split(" ")[1:]

        #the word isn't already in dictionary
        if key not in self.dict:
            self.dict[key] = values
            with open ("dictionary.txt", "a", encoding="utf-8") as file:
                file.write(f'\n{entry}')

        #the word already exists, we have to update the translation or to add it
        else:
            self.dict[key].extend(values)
            self.dict[key] = list(set(self.dict[key]))
            with open ("dictionary.txt", "w", encoding="utf-8") as file:
                for word in self.dict:
                    translation = ""
                    for trad in self.dict[word]:
                        translation += f' {trad}'
                    file.write(f'{word}{translation}\n')


    def translate(self, query):
        trads = self.dict[query]
        translation = ""
        for trad in trads:
            translation += f' {trad}'
        print(translation)

    def translateWordWildCard(self,query):
        wildCard = query.replace("?", ".") #ij this way i can use replex
        matchCounter = 0
        found = []

        for word in self.dict:
            if re.search(wildCard, word):
                found.append(word)
                matchCounter += 1

        translation = ""
        for word in found:
            translation += f' {self.dict[word]}'
        print(translation)


    def print(self):
        for key, value in self.dict.items():
            print(key, value)