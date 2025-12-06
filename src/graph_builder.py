import math
import networkx as nx
from graph_data import BERLIN_LOCATIONS, EDGES

def haversine_distance_km(coord1, coord2):
    """
    Compute the Haversine distance between two (lat, lon) pairs in kilometres.
    """
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)

    a = math.sin(d_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    return 6371 * c


def build_graph():
    """
    Build and return a weighted NetworkX graph of Berlin locations.
    """
    G = nx.Graph()

    # Add nodes with latitude and longitude
    for name, (lat, lon) in BERLIN_LOCATIONS.items():
        G.add_node(name, lat=lat, lon=lon)

    # Add edges with Haversine distance weights
    for src, dst in EDGES:
        coord_src = BERLIN_LOCATIONS[src]
        coord_dst = BERLIN_LOCATIONS[dst]
        distance = haversine_distance_km(coord_src, coord_dst)
        G.add_edge(src, dst, weight=distance)

    return G
