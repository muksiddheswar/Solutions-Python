# n, k = map(int, raw_input().strip().split(" "))
# arr = map(int, raw_input().strip().split(" "))

def nonDivisibleSubset(k, s):

    residuals = [i % k for i in s]
    counter = [0] * k
    for r in residuals:
        counter[r] += 1

    # max one element with residual 0
    c = min(counter[0], 1)

    for i in range(1, (k // 2) + 1):
        if i != k - i:
            c += max(counter[i], counter[k - i])
        else:
            c += min(counter[i], 1)

    return c

n = 7
k = 4
s = [19, 10, 12, 10, 24, 25, 22]

result = nonDivisibleSubset(k, s)
print(result)