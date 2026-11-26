from collections import deque


def solve_maze(maze, start, finish):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    previous = {start: None}
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while queue:
        cell = queue.popleft()
        if cell == finish:
            path = []
            while cell is not None:
                path.append(cell)
                cell = previous[cell]
            return path[::-1]
        for dr, dc in moves:
            nxt = (cell[0] + dr, cell[1] + dc)
            if 0 <= nxt[0] < rows and 0 <= nxt[1] < cols and maze[nxt[0]][nxt[1]] == 0 and nxt not in previous:
                previous[nxt] = cell
                queue.append(nxt)
    return []


if __name__ == "__main__":
    grid = [[0, 0, 1, 0], [1, 0, 1, 0], [0, 0, 0, 0], [0, 1, 1, 0]]
    print(solve_maze(grid, (0, 0), (3, 3)))
