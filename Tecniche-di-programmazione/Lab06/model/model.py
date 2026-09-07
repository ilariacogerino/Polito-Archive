from database.DAO import DAO

class Model:
    def __init__(self):
        self.dao = DAO()

    def getAnni(self):
        anni = self.dao.getAnni()
        return anni

    def getBrand(self):
        brands = self.dao.getBrand()
        return brands

    def getAllRetailer(self):
        retailers = self.dao.getAllRetailer()
        return retailers

    def getAllSales(self):
        sales = self.dao.getAllSales()
        return sales