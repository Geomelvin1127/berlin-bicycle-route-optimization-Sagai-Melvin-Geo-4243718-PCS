# src/visualize.py

import matplotlib.pyplot as plt
import networkx as nx
from graph_builder import build_graph


def plot_graph(G):
    """
    Plot the full graph using longitude and latitude.
    """
    plt.figure(figsize=(8, 8))

    pos = {node: (data["lon"], data["lat"]) for node, data in G.nodes(data=True)}

    nx.draw(G, pos, with_labels=True, node_size=300, font_size=8)

    plt.title("Berlin Delivery Routing Graph")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.tight_layout()
    plt.show()


def plot_route(G, path):
    """
    Highlight a specific route on the graph.
    """
    plt.figure(figsize=(8, 8))

    pos = {node: (data["lon"], data["lat"]) for node, data in G.nodes(data=True)}

    # Draw base graph
    nx.draw(G, pos, node_size=200, alpha=0.4, edge_color="gray", with_labels=False)

    # Draw highlighted route
    edges = list(zip(path, path[1:]))

    nx.draw_networkx_nodes(G, pos, nodelist=path, node_size=300)
    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=2.5)

    plt.title("Optimised Route")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    G = build_graph()
    plot_graph(G)
