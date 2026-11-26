def optimize(items, capacity):
    best = [0] * (capacity + 1)
    decisions = [[False] * (capacity + 1) for _ in items]
    for index, (weight, value) in enumerate(items):
        for room in range(capacity, weight - 1, -1):
            candidate = best[room - weight] + value
            if candidate > best[room]:
                best[room] = candidate
                decisions[index][room] = True
    selected = []
    room = capacity
    for index in range(len(items) - 1, -1, -1):
        if decisions[index][room]:
            selected.append(index)
            room -= items[index][0]
    return best[capacity], selected[::-1]


if __name__ == "__main__":
    stock = [(2, 12), (1, 10), (3, 20), (2, 15)]
    value, chosen = optimize(stock, 5)
    print(value, chosen)
