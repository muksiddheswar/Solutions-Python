
def lonelyinteger(a):
    l = [0] * len(a)
    for i in a:
        if a.count(i) == 1:
            return i
    return 0

if __name__ == '__main__':
    a = [1,1,2,2,3,3,4]
    result = lonelyinteger(a)
    print(result)