import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.getMatch=DAO.getMatch()
        self.grafo = nx.DiGraph()
        self._idMap = {}

    def creaGrafo(self, matchStringa):
        matchID=self.getMatch[matchStringa]
        self.nodi = DAO.getNodi(matchID)
        self.grafo.add_nodes_from(self.nodi)
        for v in self.nodi:
            self._idMap[v.PlayerID] = v
        self.addEdges()
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self):
        self.grafo.clear_edges()
        for nodo1 in self.grafo:
            for nodo2 in self.grafo:
                if nodo1 != nodo2 and self.grafo.has_edge(nodo1, nodo2) == False and nodo1.squadra!=nodo2.squadra:
                    diff= nodo1.efficienza-nodo2.efficienza
                    if diff>0:
                        self.grafo.add_edge(nodo1, nodo2, weight=abs(diff))
                    if diff<0:
                        self.grafo.add_edge(nodo2, nodo1, weight=abs(diff))
    def efficienzaComplessiva(self,nodo):
        entranti=0
        uscenti=0
        for arco in self.grafo.out_edges(nodo):
            uscenti+=self.grafo[arco[0]][arco[1]]["weight"]
        for arco in self.grafo.in_edges(nodo):
            entranti += self.grafo[arco[0]][arco[1]]["weight"]
        return uscenti-entranti
    def migliore(self):
        dizio={}
        for nodo in self.grafo:
            dizio[nodo.PlayerID]=self.efficienzaComplessiva(nodo)
        dizioOrder=list(sorted(dizio.items(), key=lambda item:item[1],reverse=True))
        return (self._idMap[dizioOrder[0][0]],dizioOrder[0][1])

