if __name__ == '__main':
    n, x = input().split()
    n = int(n)
    x = int(x)
    s = [int(i) for i in input().split()]
    if x > sum(s):
        print(-1)
    elif x == sum(s):
        print(n)
    else:
        if x == max(s):
            print(1)
        elif x > max(s):






