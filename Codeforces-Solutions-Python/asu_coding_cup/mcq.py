if __name__ == '__main__':
    n = input()
    s = input()
    ans = [0,0,0,0,0]
    for element in s:
        if element == 'a':
            ans[0] += 1
        elif element == 'b':
            ans[1] += 1
        elif element == 'c':
            ans[2] += 1
        elif element == 'd':
            ans[3] += 1
        else:
            ans[4] += 1
    print(min(ans), max(ans))

