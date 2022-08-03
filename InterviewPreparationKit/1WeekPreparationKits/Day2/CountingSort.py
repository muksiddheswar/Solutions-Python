

def countingSort(arr):
    counts = [0]*100
    for i in arr:
        counts[i] += 1
    return counts


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(result)