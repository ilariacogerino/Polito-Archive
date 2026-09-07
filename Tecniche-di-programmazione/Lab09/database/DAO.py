from database.DB_connect import DBConnect
from model.airport import Airport
from model.flight import Flight
from model.rotta import Rotta


class DAO():

    @staticmethod
    def getAllAirports():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        airports = []

        query = "select * from airports a"
        cursor.execute(query)

        for row in cursor:
            airports. append(Airport(**row))
        return airports

    @staticmethod
    def getAllFlights(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        flights = []

        query = "select * from flights f"
        cursor.execute(query)

        for row in cursor:
            flights.append(Flight(**row))
        return flights

    @staticmethod
    def getAllRotte():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        result = []

        query = """SELECT
                      LEAST(f.ORIGIN_AIRPORT_ID,  f.DESTINATION_AIRPORT_ID) AS a1,
                      GREATEST(f.ORIGIN_AIRPORT_ID,f.DESTINATION_AIRPORT_ID) AS a2,
                      SUM(f.DISTANCE) AS totDistance,
                      COUNT(*)        AS nVoli
                      FROM flights f
                      WHERE f.ORIGIN_AIRPORT_ID <> f.DESTINATION_AIRPORT_ID
                      GROUP BY a1, a2;"""

        cursor.execute(query)
        for row in cursor:
            result.append(Rotta(**row))
        return result
