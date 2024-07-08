import networkx as nx

S1 = nx.Graph()

# Adicionando vértices
S1.add_node('n0', label ='a', fillcolor = 'grey')
S1.add_node('n1', label ='b', fillcolor = 'blue')
S1.add_node('n2', label ='c', fillcolor = 'darkgreen')
S1.add_node('n3', label ='d', fillcolor = 'red')

# Adicionando arestas
S1.add_edge('n0','n1',label = 'ab')
S1.add_edge('n1','n2',label = 'bc')
S1.add_edge('n0','n3',label = 'ad')
S1.add_edge('n1','n3',label = 'bd')
S1.add_edge('n2','n3',label = 'cd')

# Imprimindo vértices e arestas com seus atributos
print("Vértices: ")
for n,attr_v in S1.nodes(data=True):
  print(n,attr_v)
print("Arestas: ")
for s,t,attr_e in S1.edges(data=True):
  print(s,t,attr_e)

print(S1.get_node_attributes(S1, 'label'))