class Dictionary:
    def __init__(self, dict = []):
        self._dict = dict


    def loadDictionary(self,language):
        with open (f'resources/{language}', "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                self._dict.append(line)
        return self._dict


    def printAll(self):
        for word in self._dict:
            print(word)


    @property
    def dict(self):
        return self._dict

    def __contains__(self, words):
        for word in words:
            if word in self._dict:
                return True

if __name__ == "__main__":
    d = Dictionary()
    d.loadDictionary("Italian.txt")
    d.printAll()