# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente
from model.corso import Corso


class studenteDAO:

    def getIscritti(self, codice):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("select * "
                 "from iscrizione i, studente s "
                 "where i.matricola = s.matricola and i.codins = %s")
        cursor.execute(query, (codice,))

        iscritti = []
        for row in cursor:
            iscritti.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cnx.close()
        return iscritti

    def cercaMatricola(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("select * from studente s where matricola = %s")

        cursor.execute(query, (matricola,))
        row = cursor.fetchone()
        studente = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
        cnx.close()
        return studente

    def iscrivi(self, matricola, corso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("insert into iscrizione (matricola, codins)"
                 "values (%s, %s)")
        try:
            cursor.execute(query, (matricola, corso))
            cnx.commit()
            return True
        except:
            cnx.rollback()
            return False
        cnx.close()


if __name__ == '__main__':
    studenteDAO = studenteDAO()
    iscritti = studenteDAO.getIscritti("01OVZPG")
    for iscritto in iscritti:
        print(iscritto)