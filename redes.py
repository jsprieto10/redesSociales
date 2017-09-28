import networkx as nx
import matplotlib.pyplot as plot
import pandas as pd
import csv
from networkx.algorithms import bipartite
import scipy

g = nx.Graph()

Nodes_entidades = csv.reader(open("Nodos_entidad.csv", encoding="Latin-1"), delimiter=";")
next(Nodes_entidades, None)
for row in Nodes_entidades:
	g.add_node(row[0], bipartite=0)
	row[1]
	g.node[row[0]]["Name entity "]=row[1]

Nodes_contratistas = csv.reader(open("Nodos_contratista.csv", encoding="Latin-1"), delimiter=";")
next(Nodes_contratistas, None)
for row in Nodes_contratistas:
	g.add_node(row[0], bipartite=0)
	row[1]
	g.node[row[0]]["Name workers "]=row[1]


Edges = csv.reader(open("Arcos_procesos.csv", encoding="Latin-1"), delimiter=";")
next(Edges, None)
for row in Edges:
	if (row[0] in g.nodes() and row[1] in g.nodes()):
		g.add_edge(row[0], row[1])
		g[row[0]][row[1]]["Estadod del proceso"] = row[2]
		g[row[0]][row[1]]["Objeto a contrata "] = row[3]
		g[row[0]][row[1]]["Origen de los recursos "] = row[4]
		g[row[0]][row[1]]["Valor contrato con adiciones "] = row[5]

incidence_matrix = nx.incidence_matrix(g)


print(nx.info(g))