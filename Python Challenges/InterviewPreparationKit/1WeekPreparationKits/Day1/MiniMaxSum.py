def miniMaxSum(arr):
    min_ = arr[0]
    max_ = arr[0]
    sum_ = 0
    for i in arr:
        sum_ += i
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i
    print(sum_ - max_, sum_ - min_)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
