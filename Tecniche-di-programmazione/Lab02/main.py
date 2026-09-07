import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!
    def txt_control(txt):
        txt = txt.strip()
        while any(char.isdigit() for char in txt):
            txt = input("Parola non valida, reinserirla: ")
            txt = txt.strip()
        return txt.lower()

    if int(txtIn) == 1:
        print("Quale parola vuoi aggiungere? ")
        txt = input()
        txt = txt_control(txt)
        t.handleAdd(txt)

    if int(txtIn) == 2:
        print("Di che parola vuoi sapere la traduzione?")
        txt = input()
        txt = txt_control(txt)
        t.handleTranslate(txt)

    if int(txtIn) == 3:
        print("Quale parola devo cercare?")
        txt = input()
        txt = txt_control(txt)
        t.handleWildCard(txt)

    if int(txtIn) == 4:
        print("Stampo tutto il dizionario!")
        t.handlePrint()

    if int(txtIn) == 5:
        break