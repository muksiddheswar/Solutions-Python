
def pickingNumbers(a):
    new =[]
    for i in range(0 ,n):
        new.append(a.count(a[i] ) +a.count(a[i ] +1))
        new.append(a.count(a[i] ) +a.count(a[i ] -1))
    return max(new)


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    # a = [1,1,2,2,4,4,5,5,5]
    result = pickingNumbers(a)
    print(result)
