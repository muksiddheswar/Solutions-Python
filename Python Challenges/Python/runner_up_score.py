if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # arr = [2, 3, 6, 6, 5]
    max_score = -1000
    s_max_score = -1000
    for i in arr:
        if i > max_score:
            s_max_score = max_score
            max_score = i
        elif s_max_score < i < max_score:
            s_max_score = i
    print(s_max_score)