#!/bin/python3


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    temp = 0
    # length = max(len(apples), len(apples))

    for i in apples:
        apple_position = i + a
        if s <= apple_position <= t:
            temp += 1
    print(temp)

    temp = 0
    for i in oranges:
        orange_position = i + b
        if s <= orange_position <= t:
            temp += 1
    print(temp)

    return


if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
