import random
from domanda import Domanda
from giocatore import Giocatore

file = open("domande.txt","r").read().splitlines()
domande = []

for i in range (0, len(file), 7):
    domanda = Domanda(testo=file[i], diff=file[i+1], corretta=file[i+2], opzioni=file[i+2:i+6])
    domande.append(domanda)

diff_current = 0
max_diff = max(domande, key=lambda x: x.difficolta).difficolta
flag = True
punti = 0

while flag:
    domande_possibili = [x for x in domande if int(x.difficolta)==diff_current]
    i = random.randint(0, len(domande_possibili)-1)
    domanda_corrente = domande_possibili[i]
    opzioni = domanda_corrente.mix_opzioni()
    print(domanda_corrente)
    for j in range (len(opzioni)):
        print(f'{j+1}. {opzioni[j]}')
    risposta_data = input('Inserisci la risposta: ') #sarà il numero della risposta, che corrisponde all'indice dell'opzione meno uno
    risposta = opzioni[int(risposta_data)-1]

    if risposta != domanda_corrente.corretta: #risposta sbagliata
        flag=False
        print(f'Risposta sbagliata! La risposta corretta era: {str(opzioni.index(domanda_corrente.corretta)+1)}')
        print(f'Punteggio: {str(punti)}')
        nick = input('Inserisci nickname: ')

    else: #risposta corretta
        print(f'Risposta corretta!')
        punti+=1
        diff_current+=1
        #inserisco un controllo per vedere se questa era l'ultima domanda
        if(diff_current>(int(max_diff)+1)):
            flag=False
            print(f'Hai vinto! Punteggio: {str(punti)}')
            nick = input('Inserisci nickname: ')

file = open("punti.txt","r").read().splitlines()
giocatori = []
for i in range(len(file)):
    giocatori.append(Giocatore(nickname=file[i].split(' ')[0], punti=file[i].split(' ')[1]))
giocatori.append(Giocatore(nickname=nick, punti=punti))

giocatori.sort(key=lambda x: int(x.punti), reverse=True)

with open('punti.txt','w') as file:
    for giocatore in giocatori:
        file.write(f'{giocatore.__str__()} \n')