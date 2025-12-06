import matplotlib.pyplot as plt
import networkx as nx

def plot_route(G, path):
    pos = {node: (data["lon"], data["lat"]) for node, data in G.nodes(data=True)}
    plt.figure(figsize=(8,8))

    nx.draw(G, pos, with_labels=True, node_size=300)
    route_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=route_edges, width=3)

    plt.show()
