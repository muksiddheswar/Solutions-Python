def merge_the_tools(string, k):
    length = len(string)
    index = 0
    while (index + k - 1) < length:
        u = []
        for i in range(index, index + k):
            if string[i] not in u:
                u.append(string[i])
        print(''.join(u))
        index += k


if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)