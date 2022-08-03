def flip_row(matrix, i):
    for j in range(len(matrix) // 2):
        temp = matrix[i][j]
        matrix[i][j] = matrix[i][len(matrix) - j - 1]
        matrix[i][len(matrix) - j - 1] = temp
        return matrix


def flip_column(matrix, i):
    for j in range(len(matrix) // 2):
        temp = matrix[j][i]
        matrix[j][i] = matrix[len(matrix) - j - 1][i]
        matrix[len(matrix) - j - 1][i] = temp
        return matrix


def flippingMatrix(matrix):
    for i in range(len(matrix) // 2):
        if sum(matrix[i][: i // 2]) < sum(matrix[i][i // 2:]):
            matrix = flip_row(matrix, i)

    for i in range(len(matrix) // 2):
        if sum(matrix[: i // 2])[i] < sum(matrix[i // 2:][i]):
            matrix = flip_column(matrix, i)

    for i in range(len(matrix)//2 - 1, len(matrix)):
        matrix = flip_column(matrix, i)

    for i in range(len(matrix) // 2):
        if sum(matrix[i][: i // 2]) < sum(matrix[i][i // 2:]):
            matrix = flip_row(matrix, i)

    sum1 = 0
    for i in range(len(matrix) // 2):
        sum1 += sum(matrix[:len(matrix)//2])

    return sum1


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        matrix = []
        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))
        result = flippingMatrix(matrix)
        print(result)
