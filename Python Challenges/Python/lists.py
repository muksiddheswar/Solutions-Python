if __name__ == '__main__':
    N = int(input())
    array = []
    for i in range(N):
        x = input().split()
        # l = len(x)
        command = x[0]
        if command == 'print':
            print(array)
        elif command == 'insert':
            index = int(x[1])
            e = int(x[2])
            temp = array[:index].copy()
            temp.append(e)
            temp.extend(array[index:].copy())
            array = temp.copy()
        elif command == 'remove':
            e = int(x[1])
            for index, element in enumerate(array):
                if element == e:
                    array.pop(index)
                    break
        elif command == 'append':
            e = int(x[1])
            array.append(e)
        elif command == 'sort':
            array.sort()
        elif command == 'pop':
            array.pop()
        elif command == 'reverse':
            array.reverse()