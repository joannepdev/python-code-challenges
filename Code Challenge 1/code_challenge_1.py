import random

min_n = int(input("Enter min rows: "))
max_n = int(input("Enter max rows: "))

min_m = int(input("Enter min cols: "))
max_m = int(input("Enter max cols: "))

def get_size(min_n, max_n, min_m, max_m):
    n = random.randint(min_n, max_n)
    m = random.randint(min_m, max_m)
    return n, m

n, m = get_size(min_n, max_n, min_m, max_m)
print("Generated size:", n, m)

def generate_spiral(n, m, start_row, start_col):
    visited = [[False]*m for _ in range(n)]
    path = []

    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    d = 0

    row, col = start_row, start_col

    steps = 0
    max_steps = n * m * 2

    while len(path) < n * m and steps < max_steps:
        steps += 1

        path.append((row, col))
        visited[row][col] = True

        moved = False

        for _ in range(4):
            nr = row + directions[d][0]
            nc = col + directions[d][1]

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                row, col = nr, nc
                moved = True
                break
            else:
                d = (d + 1) % 4

        if not moved:
            break

    return path

n, m = get_size(min_n, max_n, min_m, max_m)

start_row = 0
start_col = 0

path = generate_spiral(n, m, start_row, start_col)

print("Path length:", len(path))

def fill_matrix(n, m, path):
    matrix = [[0] * m for _ in range(n)]

    for i, item in enumerate(path):

        # safety check
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError(f"Invalid path element: {item}")

        row, col = item

        if 0 <= row < n and 0 <= col < m:
            matrix[row][col] = i + 1

    return matrix

matrix = fill_matrix(n, m, path)

print("Matrix:")
for row in matrix:
    print(row)