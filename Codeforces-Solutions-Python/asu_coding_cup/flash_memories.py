if __name__ =='__main__':
    nxa = input().split()
    n = int(nxa[0])
    x = int(nxa[1])
    a = int(nxa[2])
    store = a // x
    if n % store == 0:
        print(n // store)
    else:
        print(n // store + 1)