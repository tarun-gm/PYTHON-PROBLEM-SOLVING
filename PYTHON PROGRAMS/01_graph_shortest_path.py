import heapq


def shortest_paths(graph, source):
    distances = {node: float("inf") for node in graph}
    parents = {node: None for node in graph}
    distances[source] = 0
    queue = [(0, source)]
    while queue:
        distance, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue
        for neighbor, weight in graph[node]:
            if weight < 0:
                raise ValueError("Negative edges are not supported")
            candidate = distance + weight
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                parents[neighbor] = node
                heapq.heappush(queue, (candidate, neighbor))
    return distances, parents


def path_to(parents, target):
    result = []
    while target is not None:
        result.append(target)
        target = parents.get(target)
    return result[::-1]


if __name__ == "__main__":
    network = {"A": [("B", 4), ("C", 2)], "B": [("D", 5)], "C": [("B", 1), ("D", 8)], "D": []}
    distances, parents = shortest_paths(network, "A")
    print(distances)
    print(path_to(parents, "D"))
