import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._nodes = []
        self._edges = []
        self._idMap = {}
        self._nSoluzioni = 0
        self._minTassoSconfitta = 0
        self._dreamTeam = []

    def buildGraph(self, year):
        self._graph.clear()
        self._nodes = DAO.getALlDriversPerYear(year)
        self._graph.add_nodes_from(self._nodes)
        for node in self._nodes:
            self._idMap[node.driverId] = node
        self._edges = DAO.getAllEdges(year, self._idMap)
        for e in self._edges:
            self._graph.add_edge(e[0], e[1], weight=e[2])

    def getBestDriver(self):
        best = 0
        bestDriver = None
        for n in self._graph.nodes:
            score = 0
            for e_out in self._graph.out_edges(n, data=True):
                score += e_out[2]['weight']
            for e_in in self._graph.in_edges(n, data=True):
                score -= e_in[2]['weight']
            if score > best:
                best = score
                bestDriver = n
        return bestDriver, best

    def getAllAnni(self):
        anni = DAO.getAllAnni()
        return anni

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def getDreamTeam(self, k):
        self._nSoluzioni = 0
        self._minTassoSconfitta = 0
        self.ricorsione([], k)

    def getTassoSconfitta(self, parziale):
        score = 0
        for e in self._graph.edges(data=True):
            if e[0] not in parziale and e[1] in parziale:
                score += e[2]["weight"]
        return score

    def ricorsione(self, parziale, k):
        if len(parziale)>=k:
            if self.getTassoSconfitta(parziale) < self._minTassoSconfitta:
                self._minTassoSconfitta = self.getTassoSconfitta(parziale)
                self._dreamTeam = copy.deepcopy(parziale)
                return
        else:
            for n in self._graph.nodes():
                if n not in parziale:
                    parziale.append(n)
                    self.ricorsione(parziale, k)
                    parziale.pop()


