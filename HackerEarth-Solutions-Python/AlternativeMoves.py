# https://www.hackerearth.com/problem/algorithm/alternative-moves-f12ee40a/?source=list_view

T = input()
for i in range(int(T)):
    N, A, B = map(int, input().rstrip().split())
    diff = A - B
    if A >= N:
        print(1)
    elif diff < 0:
        print(-1)
    else:
        k = 1 + 2 * (- (- (N-A) // (A-B)))
        print(k)