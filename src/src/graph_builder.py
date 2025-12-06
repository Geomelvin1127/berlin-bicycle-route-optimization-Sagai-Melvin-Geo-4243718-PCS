# src/graph_builder.py

import math
import networkx as nx

from graph_data import BERLIN_LOCATIONS, EDGES


def haversine_distance_km(coord1, coord2):
    """
    Compute the Haversine distance between two (lat, lon) pairs in kilometres.
    """
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convert degrees to radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)

    # Haversine formula
    a = math.sin(d_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))

    radius_earth_km = 6371.0
    return radius_earth_km * c


def build_graph():
    """
    Build and return a NetworkX graph with Berlin locations and weighted edges.
    """
    G = nx.Graph()

    # Add nodes with coordinate attributes
    for name, (lat, lon) in BERLIN_LOCATIONS.items():
        G.add_node(name, lat=lat, l_
