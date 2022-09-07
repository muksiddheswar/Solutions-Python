def nonDivisibleSubset(k, s):
    if k == 1:
        return 1
    if k == 0:
        return 0

    largest_subset = [x % k for x in s]

    for idx in range(len(largest_subset)):
        i = largest_subset[idx]
        j = k - i
        if j in largest_subset:
            count_i = largest_subset.count(i)
            count_j = largest_subset.count(j)
            if count_j > count_i:
                largest_subset.remove(i)
            else:
                largest_subset.remove(j)
        if idx + 1 >= len(largest_subset):
            break

    return len(largest_subset)


if __name__ == '__main__':
    # n = 4
    # k = 3
    # s = [1, 7, 2, 4]

    n = 7
    k = 4
    s = [19, 10, 12, 10, 24, 25, 22]

    result = nonDivisibleSubset(k, s)
    print(result)
