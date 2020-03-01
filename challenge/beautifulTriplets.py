#!/bin/python3


# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    triplets = 0
    for i in range(len(arr) - 2):
        for j in range(i+1, len(arr) -1):
            for k in range(i+2, len(arr)):
                if (arr[j] - arr[i]) == d and (arr[k] - arr[j]) == d:
                    triplets += 1

    return triplets


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    print(result)
