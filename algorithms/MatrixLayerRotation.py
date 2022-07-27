def matrixRotation(matrix, r):
    m, n = len((matrix)), len(matrix[0])
    new_matrix = [[0]*n for _ in range(m)]

    lower = min(m, n)
    indices = []
    circles = int(lower / 2) + (lower % 2)
    for c in range(circles):
        flattened_indices = []
        for i in range(c, n - c):
            flattened_indices.append((c, i))
        for i in range(c + 1, m - 1 - c):
            flattened_indices.append((i, n - 1 - c))
        for i in range(n - c - 1, c-1, -1):
            flattened_indices.append((m - 1 - c, i))
        for i in range(m - 1 - c - 1, c, -1):
            flattened_indices.append((i, c))
        indices.append(flattened_indices)

    rotated = []
    for index in indices:
        k = r % len(index)
        rotated.append(index[k:]+index[:k])

    for (x, y) in zip(indices, rotated):
        for ((c, d), (e, f)) in zip(x, y):
            new_matrix[c][d] = matrix[e][f]

    return new_matrix


if __name__ == '__main__':
    m, n, r = map(int,input().split())
    matrix = [input().split() for i in range(m)]
    for i in matrixRotation(matrix, r):
        print(*i)