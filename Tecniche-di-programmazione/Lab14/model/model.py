import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._nodes = []
        self._edges = []
        self._idMap = {}

    def getAllStores(self):
        return DAO.getAllStores()

    def buildGraph(self, store_id, k):
        self._graph.clear()
        self._nodes = DAO.getAllOrdersByStore(store_id)
        self._graph.add_nodes_from(self._nodes)

        for node in self._nodes:
            self._idMap[node.order_id] = node

        self._edges = DAO.getAllEdges(store_id, k, self._idMap)
        for e in self._edges:
            self._graph.add_edge(e[0], e[1], weight=e[2])

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getDFSNodesFromTree(self, source):
        tree = nx.dfs_tree(self._graph, source)
        nodi = list(tree.nodes())
        return nodi[1:]

    def getCammino(self, sourceStr):
        source = self._idMap[int(sourceStr)]
        lp = [] #lista vuota che tiene il cammino più lungo trovato
        tree = nx.dfs_tree(self._graph, source)
        nodi = list(tree.nodes()) #lista dei nodi visitabili dal nodo source

        for node in nodi:
            tmp = [node] #lista che contiene il cammino del source fino a questo nodo
            while tmp[0] != source:
                pred = nx.predecessor(tree, source, tmp[0]) #trova il predecessore del nodo corrente nel cammino da source
                tmp.append(pred[0])
            if len(tmp) > len(lp):
                lp = copy.deepcopy(tmp)
        return lp

