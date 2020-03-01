

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    swaps = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if (i == arr[i] - 1) or visited[i] == True:
            continue
        else:
            loop = 0
            j = i
            while visited[j] != True:
                visited[j] = True
                loop += 1
                j = arr[j] - 1

            if loop > 0:
                swaps += loop - 1
    return swaps


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    print(res)