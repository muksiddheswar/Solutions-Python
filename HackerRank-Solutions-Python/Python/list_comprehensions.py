if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # x = 1
    # y = 1
    # z = 2
    # n = 3

    d = [[a, b, c] for a in range(x + 1)
         for b in range(y + 1)
         for c in range(z + 1) if a + b + c != n]
    print(d)
