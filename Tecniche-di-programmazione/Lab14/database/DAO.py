from database.DB_connect import DBConnect
from model.order import Order


class DAO():

    @staticmethod
    def getAllStores():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select s.store_id from stores s  """
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(row["store_id"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getAllOrdersByStore(store_id):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select *
                    from orders o
                    where o.store_id = %s """
        cursor.execute(query, (store_id,))

        result = []
        for row in cursor:
            result.append(Order(**row))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getAllEdges(store_id, k, idMap):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select distinct o1.order_id as o1, o2.order_id as o2, count(oi1.quantity + oi2.quantity) as cnt
                    from orders o1 , orders o2, order_items oi1, order_items oi2
                    where o1.store_id = %s
                    and o1.store_id = o2.store_id 
                    and datediff(o1.order_date, o2.order_date)  < %s
                    and o1.order_date > o2.order_date 
                    and o1.order_id = oi1.order_id 
                    and o2.order_id = oi2.order_id 
                    group by o1, o2"""
        cursor.execute(query, (store_id, k,))

        result = []
        for row in cursor:
            result.append((idMap[row["o1"]], idMap[row["o2"]], row["cnt"]))
        cursor.close()
        cnx.close()
        return result
