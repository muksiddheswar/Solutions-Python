
def pageCount(n, p):
    fullPages = (n - 2) // 2
    fullPageNumber = p // 2
    if fullPageNumber <= fullPages // 2:
        return fullPageNumber
    else:
        return fullPages - fullPageNumber + 1

if __name__ == '__main__':
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    print(result)