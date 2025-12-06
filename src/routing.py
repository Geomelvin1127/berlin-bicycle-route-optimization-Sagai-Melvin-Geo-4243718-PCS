import networkx as nx
from graph_builder import build_graph, haversine_distance_km
from graph_data import BERLIN_LOCATIONS

def astar_heuristic(u, v):
    return haversine_distance_km(BERLIN_LOCATIONS[u], BERLIN_LOCATIONS[v])

def shortest_path_dijkstra(G, source, target):
    path = nx.dijkstra_path(G, source, target, weight="weight")
    dist = nx.path_weight(G, path, weight="weight")
    return path, dist

def shortest_path_astar(G, source, target):
    path = nx.astar_path(G, source, target, heuristic=astar_heuristic, weight="weight")
    dist = nx.path_weight(G, path, weight="weight")
    return path, dist
