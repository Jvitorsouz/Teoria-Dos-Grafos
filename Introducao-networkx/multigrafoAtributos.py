import networkx as nx

M1 = nx.MultiGraph()

# Adicionando vértices
M1.add_node('n0', label ='a', fillcolor = 'grey')
M1.add_node('n1', label ='b', fillcolor = 'blue')
M1.add_node('n2', label ='c', fillcolor = 'darkgreen')
M1.add_node('n3', label ='d', fillcolor = 'red')

# Adicionando arestas
M1.add_edge('n0','n1',label = 'ab')
M1.add_edge('n1','n2',label = 'bc')
M1.add_edge('n0','n3',label = 'ad')
M1.add_edge('n1','n3',label = 'bd')
M1.add_edge('n2','n3',label = 'cd1')
M1.add_edge('n2','n3',label = 'cd2')

# Imprimindo vértices e arestas com seus atributos
print("Vértices: ")
for n,attr_v in M1.nodes(data=True):
  print(n,attr_v)
print("Arestas: ")
for s,t,i in M1.edges:
  print(s,t,i,M1.get_edge_data(s,t,i))