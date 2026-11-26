from collections import deque


def connected_components(graph):
    unseen = set(graph)
    components = []
    while unseen:
        start = unseen.pop()
        component = {start}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph.get(node, []):
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    component.add(neighbor)
                    queue.append(neighbor)
        components.append(sorted(component))
    return components


def degrees(graph):
    result = {node: len(neighbors) for node, neighbors in graph.items()}
    for neighbors in graph.values():
        for neighbor in neighbors:
            result.setdefault(neighbor, 0)
    return result


def is_tree(graph):
    nodes = set(graph)
    for neighbors in graph.values():
        nodes.update(neighbors)
    if not nodes:
        return True
    components = connected_components(graph)
    edge_count = sum(len(neighbors) for neighbors in graph.values()) // 2
    return len(components) == 1 and edge_count == len(nodes) - 1


if __name__ == "__main__":
    topology = {"router": ["switch"], "switch": ["router", "pc-1", "pc-2"], "pc-1": ["switch"], "pc-2": ["switch"], "isolated": []}
    print("Components:", connected_components(topology))
    print("Degrees:", degrees(topology))
    print("Is tree:", is_tree(topology))
