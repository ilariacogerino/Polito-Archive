from model.model import Model

myModel = Model()
myModel.buildGraph()

print(myModel.getNumNodes()) #322
print(myModel.getNumEdges())