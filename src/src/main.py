# src/main.py

from graph_builder import build_graph
from routing import shortest_path_dijkstra, shortest_path_astar
from multi_stop import nearest_neighbour_route
from visualize import plot_route


def single_route_demo(G):
    source = "Brandenburg Gate"
    target = "Alexanderplatz"

    dij_path, dij_dist = shortest_path_dijkstra(G, source, target)
    astar_path, astar_dist = shortest_path_astar(G, source, target)

    print("\n=== Single Route Demo ===")
    print("Dijkstra:", " -> ".join(dij_path), "| Distance:", round(dij_dist, 2), "km")
    print("A*      :", " -> ".join(astar_path), "| Distance:", round(astar_dist, 2), "km")

    plot_route(G, astar_path)


def multi_stop_demo(G):
    start = "Brandenburg Gate"
    stops = ["Museum Island", "Alexanderplatz", "Treptower Park", "Mauerpark"]

    route, dist = nearest_neighbour_route(G, start, stops)

    print("\n=== Multi-Stop Route Demo ===")
    print("Route:", " -> ".join(route))
    print("Total Distance:", round(dist, 2), "km")

    plot_route(G, route)


if __name__ == "__main__":
    G = build_graph()
    single_route_demo(G)
    multi_stop_demo(G)
