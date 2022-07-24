def left_column_elements(matrix, new_matrix, corner_i, corner_j, m, n, displacement):
    for i in range(m):
        # Column Element
        if displacement <= (m - 1 - i):
            i_index = i + displacement
            i_index += corner_i
            j_index = corner_j

        elif (m - 1 - i) < displacement <= (m + n - 2 - i):
            i_index = m - 1 + corner_i
            j_index = displacement - m + 1 + i
            j_index += corner_j

        elif (m + n - 2 - i) < displacement <= ((2 * m) + n - 3 - i):
            i_index = m - 1 - (displacement - (m + n - 2 - i))
            i_index += corner_i
            j_index = n - 1 + corner_j

        elif ((2 * m) + n - 3 - i) < displacement <= ((2 * m) + (2 * n) - 4 - i):
            i_index = corner_i
            j_index = m - 1 - (displacement - ((2 * m) + n - 3 - i))
            j_index += corner_j

        else:
            i_index = displacement - ((2 * m) + (2 * n) - 4 - i) - 1
            i_index += corner_i
            j_index = corner_j

        new_matrix[i_index][j_index] = matrix[corner_i + i][corner_j]

def matrixRotation(matrix, r):
    m = len((matrix))
    n = len(matrix[0])
    new_matrix = [[0]*n]*m
    if m <= n :
        lower = m
    else:
        lower = n
    circles = int(lower / 2) + (lower % 2)
    corner_i = 0
    corner_j = 0

    for circle in range(circles):
        if n == m == 1:
            # single element
            # no change
            i_index = corner_i
            j_index = corner_j
            new_matrix[i_index][j_index] = matrix[i_index][j_index]

        else:
            circumference = (2*m) + (2*n) - 4
            displacement = r % circumference
            if displacement == 0:

                # No change for this circle
                j = 0
                for i in range(m):
                    # Column Element
                    new_matrix[corner_i + i][corner_j + j] = matrix[corner_i + i][corner_j + j]

                for j in range(n):
                    # Row Element
                    new_matrix[corner_i + i][corner_j + j] = matrix[corner_i + i][corner_j + j]

                for i in range(m - 1, -1, -1):
                    # Column Element
                    new_matrix[corner_i + i][corner_j + j] = matrix[corner_i + i][corner_j + j]

                for j in range(n - 1, -1, -1):
                    # Row Element
                    new_matrix[corner_i + i][corner_j + j] = matrix[corner_i + i][corner_j + j]

            else:
                if m == 1:
                    # Row Matrix
                    pass

                elif n == 1:
                    # Column Matrix
                    pass

                else:

                    for i in range(m):
                        # Column Element
                        if displacement <= (m-1-i):
                            i_index = i + displacement
                            i_index += corner_i
                            j_index = corner_j

                        elif (m - 1 - i) < displacement <= (m + n - 2 - i):
                            i_index = m-1 + corner_i
                            j_index = displacement - m + 1 + i
                            j_index += corner_j

                        elif (m + n - 2 - i) < displacement <= ((2*m) + n - 3 - i):
                            i_index = m - 1 - (displacement - (m + n - 2 - i))
                            i_index += corner_i
                            j_index = n - 1 + corner_j

                        elif ((2 * m) + n - 3 - i) < displacement <= ((2 * m) + (2 * n) - 4 - i):
                            i_index = corner_i
                            j_index = m - 1 - (displacement - ((2 * m) + n - 3 - i))
                            j_index += corner_j

                        else:
                            i_index = displacement - ((2 * m) + (2 * n) - 4 - i) - 1
                            i_index += corner_i
                            j_index = corner_j

                        # a = new_matrix[i_index][j_index]
                        b = matrix[corner_i + i][corner_j]
                        new_matrix[i_index][j_index] = b

                    for j in range(n):
                        # Row Element
                        if displacement <= (n - 1 - j):
                            i_index = i + corner_i
                            j_index = j + displacement
                            j_index += corner_j

                        elif (n - 1 - j) < displacement <= (m + n - 2 - j):
                            i_index = m - 1 - (displacement - (n - 1 - j))
                            i_index += corner_i
                            j_index = n - 1 + corner_j

                        elif (m + n - 2 - j) < displacement <= ((2*n) + m - 3 - j):
                            i_index = corner_i
                            j_index = n - 1 - (displacement - (m + n - 2 - j))
                            j_index += corner_j

                        elif ((2*n) + m - 3 - j) <= displacement <= ((2 * m) + (2 * n) - 4 - j):
                            i_index = displacement - ((2*n) + m - 3 - j)
                            i_index += corner_i
                            j_index = corner_j

                        else:
                            i_index = m - 1 + corner_i
                            j_index = displacement - ((2 * m) + (2 * n) - 4 - j)
                            j_index += corner_j

                        new_matrix[i_index][j_index] = matrix[corner_i][corner_j + j]

                    for i in range(m-1, -1, -1):
                        # Column Element
                        if displacement <= i:
                            i_index = i - displacement
                            i_index += corner_i
                            j_index = n - 1 + corner_j

                        elif i < displacement <= (m - 1 + i):
                            i_index = corner_i
                            j_index = m - 1 - (displacement - i)
                            j_index += corner_j

                        elif (m - 1 + i) < displacement <= (m + n - 2 + i):
                            i_index = displacement - (m - 1 + i)
                            i_index += corner_i
                            j_index = corner_j

                        elif (m + n - 2 + i) < displacement <= ((2 * m) + n - 3 + i):
                            i_index = n - 1 + corner_i
                            j_index = displacement - (m + n - 2 + i)
                            j_index += corner_j

                        else:
                            i_index = m - 1 - (displacement - ((2 * m) + n - 3 + i))
                            i_index += corner_i
                            j_index = n - 1 + corner_j

                        new_matrix[i_index][j_index] = matrix[corner_i + i][corner_j]

                    for j in range(n-1, -1, -1):
                        # Row Element
                        if displacement <= j:
                            i_index = corner_i
                            j_index = j - displacement
                            j_index += corner_j

                        elif j < displacement <= (m - 1 + j):
                            i_index = displacement - j
                            i_index += corner_i
                            j_index = corner_j

                        elif (m - 1 + j) < displacement <= (m + n - 2 + j):
                            i_index = m-1 + corner_i
                            j_index = displacement - (m - 1 + j)
                            j_index += corner_j

                        elif (m + n - 1 + j) < displacement <= ((2 * m) + n - 3 + j):
                            i_index = m - 1 - (displacement - (m + n - 1 + j))
                            i_index += corner_i
                            j_index = n - 1 + corner_j

                        else:
                            i_index = corner_i
                            j_index = n - 1 - (displacement - ((2 * m) + n - 3 + j))
                            j_index += corner_j

                        print(i_index,j_index)
                        new_matrix[i_index][j_index] = matrix[corner_i][corner_j + j]

        m -= 2
        n -= 2
        corner_i += 1
        corner_j += 1


    for i in range(len(matrix)):
        print(' '.join(str(x) for x in matrix[i]))


if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()
    #
    # m = int(first_multiple_input[0])
    #
    # n = int(first_multiple_input[1])
    #
    # r = int(first_multiple_input[2])
    #
    # matrix = []
    #
    # for _ in range(m):
    #     matrix.append(list(map(int, input().rstrip().split())))

    matrix = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    matrixRotation(matrix, 5)
