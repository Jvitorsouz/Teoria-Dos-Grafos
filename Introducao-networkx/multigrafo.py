import networkx as nx

M =  nx.MultiGraph()

M.add_nodes_from(['a', 'b'])
#M.add_edges_from([('x','y'),('x','y'),('y','x'),('x','w'), ('y','w'),('z','w'),('w','z')])
print(f"Vértices: {M.nodes(data=True)}")
print(f"Arestas: {M.edges()}")