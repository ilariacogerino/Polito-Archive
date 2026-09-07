from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.sale import Sale

class DAO():

    def getAnni(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = "select distinct year(Date) from go_daily_sales gds"
        cursor.execute(query)
        rows = cursor.fetchall()
        anni = []
        for row in rows:
            anni.append(int(row[0]))
        cursor.close()
        cnx.close()
        return anni

    def getBrand(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = "select distinct Product_brand from go_products gp"
        cursor.execute(query)
        rows = cursor.fetchall()
        brands = []
        for row in rows:
            brands.append(row[0])
        cursor.close()
        cnx.close()
        return brands

    def getAllRetailer(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "select * from go_retailers gr"
        cursor.execute(query)
        retailers = []
        for row in cursor:
            retailers.append(Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"]))
        cursor.close()
        cnx.close()
        return retailers

    def getAllSales(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("select gds.Retailer_code, gp.Product_number, Product_brand, Date, Quantity, Unit_sale_price, Unit_sale_price * Quantity AS Revenue "
                 "from go_daily_sales gds, go_products gp "
                 "where gds.Product_number = gp.Product_number "
                 "order by revenue DESC")
        cursor.execute(query)
        sales = []
        for row in cursor:
            sales.append(Sale(row["Retailer_code"], row["Product_number"], row["Product_brand"], row["Date"], row["Quantity"], row["Unit_sale_price"], row["Revenue"]))
        cursor.close()
        cnx.close()
        return sales



