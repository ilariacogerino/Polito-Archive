import copy

from database.meteo_dao import MeteoDao

class Model:
    def __init__(self):
        self.dao = MeteoDao()

    def getSituazioni(self, localita, mese):
        situazioni = self.dao.getSituazioniCittaMese(localita, mese)
        return situazioni


    def calcola_sequenza(self, mese):
        self.n_soluzioni = 0
        self.costo_ottimo = -1
        self.soluzione_ottima = []
        situazioni = self.dao.getSituazioni15ggMese(mese)
        self.ricorsione([], situazioni)
        return self.soluzione_ottima, self.costo_ottimo


    def get_next_steps(self, parziale, lista_situazioni):
        #ritorno una lista che possiede le info del giorno successivo nelle tre località
        giorno = len(parziale)+1
        steps = []
        for situazione in lista_situazioni:
            if situazione.data.day == giorno:
                steps.append(situazione)
        return steps


    def is_admissible(self, step, parziale):
        #inserisco tutti i vincoli del problema

        #vincolo sui 6 giorni
        counter = 0
        for situazione in parziale:
            if situazione.localita == step.localita:
                counter += 1
        if counter>=6:
            return False

        #vincolo sulla permanenza
            # 1) parziale è minore di 3 quindi il tecnico non può muoversi
        if len(parziale)==0:
            return True
        if len(parziale)<3:
            if step.localita != parziale[0].localita:
                return False

            # 2) le tre situaizoni precedenti non sono tutte uguali
        else:
            if parziale[-3].localita != parziale[-2].localita or \
                parziale[-3].localita != parziale[-1].localita or \
                parziale[-1].localita != parziale[-2].localita:
                if parziale[-1].localita != step.localita:
                    return False
        return True


    def calcola_costo(self, parziale):
        costo = 0
        for situazione in parziale:
            costo += situazione.umidita
        return costo


    def ricorsione(self, parziale, lista_situazioni):
        if len(parziale) == 15: #condizione finale
            self.n_soluzioni += 1
            costo = self.calcola_costo(parziale)
            if self.costo_ottimo == -1 or self.costo_ottimo > costo:
                self.costo_ottimo = costo
                self.soluzione_ottima = copy.deepcopy(parziale)
        else: #condizione ricorsiva
            #cerco possibili step successivi
            next_steps = self.get_next_steps(parziale, lista_situazioni)
            #provo ad aggiungere uno di questi step
            for step in next_steps:
                if self.is_admissible(step, parziale):
                    parziale.append(step)
                    self.ricorsione(parziale, lista_situazioni)
                    parziale.pop() #backtracking
        return self.soluzione_ottima, self.costo_ottimo