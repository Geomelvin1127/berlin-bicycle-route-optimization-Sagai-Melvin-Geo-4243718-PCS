from routing import shortest_path_dijkstra

def nearest_neighbour_route(G, start, stops):
    remaining = set(stops)
    current = start
    route = [current]
    total_dist = 0

    while remaining:
        best = None
        best_dist = float("inf")

        for candidate in remaining:
            _, dist = shortest_path_dijkstra(G, current, candidate)
            if dist < best_dist:
                best = candidate
                best_dist = dist

        route.append(best)
        total_dist += best_dist
        remaining.remove(best)
        current = best

    return route, total_dist
