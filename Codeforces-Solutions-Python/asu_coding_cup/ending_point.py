if __name__ == '__main__':
    x, y = input().split()
    x = int(x)
    y = int(y)
    s = input()
    for element in s:
        if element == 'U':
            y += 1
        elif element == 'D':
            y -= 1
        elif element == 'L':
            x -= 1
        else:
            x += 1
    print('%s %s'%(x,y))
