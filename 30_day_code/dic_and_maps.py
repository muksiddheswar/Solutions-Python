if __name__ == '__main__':
    n = int(input())
    store = {}
    for i in range(n):
        user_input = input().rstrip().split()
        store[user_input[0]] = user_input[1]
    while True:
        try:
            name = input()
            if name in store:
                print('%s=%s' % (name, store[name]))
            else:
                print('Not found')
        except:
            break
