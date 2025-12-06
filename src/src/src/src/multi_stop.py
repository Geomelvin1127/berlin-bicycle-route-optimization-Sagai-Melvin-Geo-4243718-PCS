# src/multi_stop.py

from typing import List, Tuple
from graph_builder import build_graph
from routing import shortest_path_dijkstra


def nearest_neighbour_route(G, start: str, stops: List[str]) -> Tuple[List[str], float]:
    """
    Construct a multi-stop route using a nearest-neighbour heuristic.

    :param G: NetworkX graph
    :param start: Starting location node
    :param stops: List of target nodes
    :return: (ordered route including start and all stops, total_distance_km)
    """
    remaining = set(stops)
    current = start
    route = [current]
    total_distance = 0.0

    while remaining:
        best_stop = None
        best_distance = float("inf")

        for candidate in remaining:
            _, dist = shortest_path_dijkstra(G, current, candidate)
            if dist < best_distance:
                best_distance = dist
                best_stop = candidate

        # Move to selected stop
        route.append(best_stop)
        total_distance += best_distance
        remaining.remove(best_stop)
        current = best_stop

    return route, total_distance


if __name__ == "__main__":
    G = build_graph()
    start = "Brandenburg Gate"
    stops = ["Museum Island", "Alexanderplatz", "Treptower Park", "Mauerpark"]

    route, dist = nearest_neighbour_route(G, start, stops)
    print("Route:", " -> ".join(route))
    print("Total Distance:", round(dist, 2), "km")
