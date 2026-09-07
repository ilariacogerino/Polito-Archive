# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso

class corsoDAO:

    def getAllCorsi(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query="select * from corso"
        cursor.execute(query)

        corsi = []
        for row in cursor:
            corsi.append(Corso(row["codins"], row["crediti"],row["nome"], row["pd"]))
        cnx.close()
        return corsi

    def getCorsi(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("select * from corso c, iscrizione i "
                 "where c.codins = i.codins and i.matricola = %s")

        cursor.execute(query, (matricola,))
        corsi = []
        for row in cursor:
            corsi.append(Corso(row["codins"], row["crediti"],row["nome"], row["pd"]))
        cnx.close()
        return corsi


if __name__ == "__main__":
   corsoDAO = corsoDAO()
   corsi = corsoDAO.getAllCorsi()
   for corso in corsi:
       print(corso)