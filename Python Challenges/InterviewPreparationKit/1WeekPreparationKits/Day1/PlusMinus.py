def plusMinus(arr):
    # Write your code here
    p = n = o = 0
    for i in arr:
        if i == 0:
            o += 1
        elif i > 0:
            p += 1
        else:
            n += 1
    all = p+n+o
    print('%.6f' % (p / all))
    print('%.6f' % (n / all))
    print('%.6f' % (o / all))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
