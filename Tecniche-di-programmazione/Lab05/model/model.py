from database.corso_DAO import corsoDAO
from database.studente_DAO import studenteDAO

class Model:
    def __init__(self):
        self.daoC = corsoDAO()
        self.daoS = studenteDAO()

    def getAllCorsi(self):
        corsi = self.daoC.getAllCorsi()
        return corsi

    def getIscritti(self, corso):
        iscritti = self.daoS.getIscritti(corso)
        return iscritti

    def getMatricola(self, matricola):
        studente = self.daoS.cercaMatricola(matricola)
        return studente

    def getCorsi(self, matricola):
        corsi = self.daoC.getCorsi(matricola)
        return corsi

    def iscrivi(self, matricola, corso):
        esito = self.daoS.iscrivi(matricola, corso)
        return esito


if __name__ == '__main__':
    m = Model()
    iscritti = m.getIscritti("01OVZPG")
    for i in iscritti:
        print(i)

