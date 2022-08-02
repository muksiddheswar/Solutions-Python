# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    actual = [
                [8, 1, 6, 3, 5, 7, 4, 9, 2],
                [6, 1, 8, 7, 5, 3, 2, 9, 4],
                [4, 9, 2, 3, 5, 7, 8, 1, 6],
                [2, 9, 4, 7, 5, 3, 6, 1, 8],
                [8, 3, 4, 1, 5, 9, 6, 7, 2],
                [4, 3, 8, 9, 5, 1, 2, 7, 6],
                [6, 7, 2, 1, 5, 9, 8, 3, 4],
                [2, 7, 6, 9, 5, 1, 4, 3, 8]
            ]
    cost = []
    for matrix in actual:
        p_cost = 0
        index = 0
        for ri in range(3):
            for ci in range(3):
                p_cost += abs(matrix[index] - s[ri][ci])
                index += 1
        cost.append(p_cost)
    return min(cost)



if __name__ == '__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)