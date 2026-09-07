from database.DB_connect import DBConnect
from model.situazione import Situazione


class MeteoDao():

    @staticmethod
    def getSituazioniCittaMese(localita, mese):
        cnx = DBConnect.get_connection()
        situazioni = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select Localita, Data, Umidita 
            from situazione s 
            where Localita = %s and month(Data) = %s"""
            cursor.execute(query, (localita, mese))
            for row in cursor:
                situazioni.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return situazioni

    def getSituazioni15ggMese(self, mese):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("select Localita, Data, Umidita "
                 "from situazione s "
                 "where month(Data)= %s and day(Data)<16")
        cursor.execute(query, (mese,))
        situazioni = []
        for row in cursor:
            situazioni.append(Situazione(row["Localita"], row["Data"], row["Umidita"]))
        cursor.close()
        cnx.close()
        return situazioni



if __name__ == '__main__':
    meteoDao = MeteoDao()
    situazioni = meteoDao.getSituazioniCittaMese("Milano", 1)
    for sit in situazioni:
        print(sit)



