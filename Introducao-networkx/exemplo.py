import networkx as nx
import matplotlib.pyplot as plt

#Necessario clonar o repositorio dentro dessa pasta
#git clone https://github.com/pdlmachado/gtufcg.git
from gtufcg.util.draw_util import draw_graph
from gtufcg.util.import_util import read_multiple_CSV


S = nx.Graph()
print(f"Grafo nulo: {S}")

S.add_nodes_from(['x','y', 'z', 'w'])
S.add_node('a')
print(f"Vértices: {S.nodes}")

S.add_edges_from([('x', 'y'), ('x', 'w'), ('x', 'z'), ('y', 'z')])
S.add_edge('a', 'x')
print(f"Arestas: {S.edges}")

draw_graph(S)
