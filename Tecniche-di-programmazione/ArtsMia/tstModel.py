from model.model import Model

myModel = Model()

myModel.buildGraph()
print(f'N nodi: {myModel.getNumNodes()}')
print(f'N edges: {myModel.getNumEdges()}')

myModel.getInfoConnessa(1234)