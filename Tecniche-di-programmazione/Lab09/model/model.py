import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.DiGraph()
        self._nodes = None
        self._edges = None
        self._idMap = {}


    def buildGraph(self, min):
        self._graph.clear()
        self._nodes = DAO.getAllAirports()
        self.fillIdMap()
        self._graph.add_nodes_from(self._nodes)
        self.addEdgesPesati(min)


    def getNumNodes(self):
        return self._graph.number_of_nodes()


    def getNumEdges(self):
        return self._graph.number_of_edges()


    def addEdgesPesati(self, min):
        self._edges = DAO.getAllRotte()
        for edge in self._edges:
            airport1 = self._idMap[edge.a1]
            airport2 = self._idMap[edge.a2]
            avgDistance = edge.totDistance / edge.nVoli
            if avgDistance>int(min):
                self._graph.add_edge(airport1, airport2, weight=avgDistance)


    def fillIdMap(self):
        for node in self._nodes:
            self._idMap[node.ID] = node

