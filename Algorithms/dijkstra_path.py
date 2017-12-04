import networkx as nx
import numpy as np
A = np.array([[0,1,0,0,1],
             [2,0,2,2,3],
             [0,1,0,1,0],
             [0,3,1,0,1],
             [1,1,0,1,0]])
G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
print(nx.dijkstra_path(G, 0, 3))
