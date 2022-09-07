def divisibleSumPairs(n, k, ar):
    number = 0
    for j in range(n):
        for i in range(j):
            if (ar[i] + ar[j]) % k ==0:
                number += 1
    return number


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
