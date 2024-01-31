
if __name__ == '__main__':
    a, b = input().split()
    a = int(a)
    b = int(b)
    a_val = a
    b_val = b
    while a_val != b_val:
        if a_val < b_val:
            a_val += a
        else:
            b_val += b
    print(a_val)