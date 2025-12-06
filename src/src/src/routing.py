# src/routing.py

import networkx as nx
from graph_builder import build_graph, haversine_distance_km
from graph_data import BERLIN_LOCATIONS


def astar_heuristic(u, v):
    """
    Heuristic for A*: straight-line (Haversine) distance between u and v.
    """
    coord_u = BERLIN_LOCATIONS[u]
    coord_v = BERLIN_LOCATIONS[v]
    return haversine_distance_km(coord_u, coord_v)


def shortest_path_dijkstra(G, source, target):
    """
    Compute shortest path using Dijkstra's algorithm.
    Returns (path, total_distance_km).
    """
    path = nx.dijkstra_path(G, source, target, weight="weight")
    distance = nx.path_weight(G, path, weight="weight")
    return path, distance


def shortest_path_astar(G, source, target):
    """
    Compute shortest path using A* algorithm.
    Returns (path, total_distance_km).
    """
    path = nx.astar_path(G, source, target, heuristic=astar_heuristic, weight="weight")
    distance = nx.path_weight(G, path, weight="weight")
    return path, distance


if __name__ == "__main__":
    # Manual test
    G = build_graph()
    p, d = shortest_path_dijkstra(G, "Brandenburg Gate", "Alexanderplatz")
    print("Dijkstra:", p, "Distance:", round(d, 2))

    p2, d2 = shortest_path_astar(G, "Brandenburg Gate", "Alexanderplatz")
    print("A*:", p2, "Distance:", round(d2, 2))
