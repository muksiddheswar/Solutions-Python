def hurdleRace(k, height):
    max_height = max(height)
    if  max_height - k > 0:
        return max_height - k
    else:
        return 0

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    height = list(map(int, input().rstrip().split()))
    result = hurdleRace(k, height)
    print(result)


