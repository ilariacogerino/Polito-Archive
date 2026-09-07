from database.DB_connect import DBConnect
from model.driver import Driver


class DAO():

    @staticmethod
    def getAllAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select distinct s.year from seasons s """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row["year"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getALlDriversPerYear(year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select distinct d.*
                    from drivers d, results r, races r2 
                    where d.driverId = r.driverId
                    and r.raceId = r2.raceId 
                    and r2.`year` = %s
                    and r.`position` is not null"""
        cursor.execute(query, (year,))
        result = []
        for row in cursor:
            result.append(Driver(**row))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getAllEdges(year, idMap):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select r.driverId as r1, r2.driverId as r2, count(*) as cnt
                    from results r , results r2 , races r3 
                    where r3.`year` = %s
                    and r.raceId = r3.raceId 
                    and r2.raceId = r3.raceId 
                    and r.position is not null
                    and r2.`position` is not null
                    and r.position<r2.`position` 
                    group by r1, r2"""
        cursor.execute(query, (year,))
        result = []
        for row in cursor:
            result.append((idMap[row["r1"]], idMap[row["r2"]], row["cnt"]))
        cursor.close()
        cnx.close()
        return result
