import networkx as nx
import matplotlib.pyplot as plt

# graph 만들고
G = nx.Graph()

# add node
G.add_node(1)
G.add_nodes_from([2, 3])

# add edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# show graph
nx.draw(G)
plt.show()
