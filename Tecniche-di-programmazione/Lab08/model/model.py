import copy

from database.DAO import DAO


class Model:
    def __init__(self):
        # inizializzazione
        self._solBest = []
        self._clientiMaxBest = 0
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()


    def worstCase(self, nerc, maxY, maxH):
        self.loadEvents(nerc)
        self.ricorsione([], maxY, maxH, 0)
        print(self._solBest)


    def ricorsione(self, parziale, maxY, maxH, pos):
        #condizione finale
        if self.sumDurata(parziale)/60/60 > maxH:
            return

        #verifico se la soluzione è la migliore tramite i clienti
        if self.countCustomers(parziale) > self._clientiMaxBest:
            self._solBest = copy.deepcopy(parziale)
            self._clientiMaxBest = self.countCustomers(parziale)

        #ricorsione
        i = pos #serve per evitare doppioni e ridurre lo spazio di ricerca; i dati devo essere ordinati per data
        for e in self._listEvents[pos:]:
            parziale.append(e)
            if self.getRangeAnni(parziale) > maxY:
                parziale.remove(e)
                return
            i+=1
            self.ricorsione(parziale, maxY, maxH, i)
            parziale.pop() #backtracking


    def getRangeAnni(self, parziale):
        if len(parziale) < 2:
            return 0
        first = parziale[0].date_event_began
        last = parziale[-1].date_event_finished

        return int(last.year - first.year)


    def countCustomers(self, parziale):
        if len(parziale) == 0:
            return 0
        customer = 0
        for event in parziale:
            customer += event.customers_affected
        return customer


    def sumDurata(self, parziale):
        if len(parziale) == 0:
            return 0
        sum = 0
        for event in parziale:
            sum += self.durata(event)
        return sum


    def durata(self, event):
        return (event.date_event_finished - event.date_event_began).total_seconds()


    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)


    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc