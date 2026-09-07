import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMap = {}
        for v in self._nodes:
            self._idMap[v.object_id] = v

    def getInfoConnessa(self, idInput):
        """
        identifica la componente connessa che
        contiene idInput e ne restituisce la dimensione
        """
        if not self.hasNode(idInput): #conrollo ridondante
            return None

        source = self._idMap[idInput] #prendo l'oggetto

        #modo 1: conto i successori, non è corretto
        """succ = nx.dfs_successors(self._graph, source).values() #dizionario che ha come chiave un oggetto e come valore tutti gli oggetti a cui posso arrivare
        res = []
        for s in succ:
            res.extend(s)
        print("Size connessa con modo 1: ", len(res))"""

        """#modo 2: conto i predecessori
        pred = nx.dfs_predecessors(self._graph, source)
        print("Size connessa con modo 2: ", len(pred.values()))"""

        """#modo 3: conto i nodi dell'albero di visita, il migliore (bisogna togliere uno perchè conta anche il nodo source)
        dfsTree = nx.dfs_tree(self._graph, source)
        print("Size connessa con modo 3: ", len(dfsTree.nodes()))"""

        #modo 4: uso il metodo nodes connected
        conn = nx.node_connected_component(self._graph, source)
        print("Size connessa con modo 4: ", len(conn))

        return len(conn)


    def hasNode(self, idInput):
        #verifica che nel grafo ci sia quel nodo
        #return idInput in self._graph #se ho l'oggetto posso controllare direttamente se esiste nel grafo
        return idInput in self._idMap #controllo se l'ggetto esiste nella mappa, non nel grafo

    def buildGraph(self):
        nodes = DAO.getAllNodes()
        self._graph.add_nodes_from(nodes)
        self.addAllEdges()

    def addEdgesV1(self):
        for u in self._nodes:
            for v in self._nodes:
                peso = DAO.getPeso(u,v)
                if peso != 0:
                    self._graph.add_edge(u, v, weight=peso)


    def addAllEdges(self):
        allEdges = DAO.getAllArchi(self._idMap)
        for e in allEdges:
            self._graph.add_edge(e.o1, e.o2, weight=e.peso)


    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getIdMap(self):
        return self._idMap

    def getObjectFromId(self, idInput):
        return self._idMap[idInput]