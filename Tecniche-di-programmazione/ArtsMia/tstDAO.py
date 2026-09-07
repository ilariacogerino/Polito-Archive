from database.DAO import DAO
from model.model import Model

listObject = DAO.getAllNodes()
mymodel = Model()
mymodel.buildGraph()

print(len(listObject))

edges = DAO.getAllArchi(mymodel.getIdMap())

print(len(edges))