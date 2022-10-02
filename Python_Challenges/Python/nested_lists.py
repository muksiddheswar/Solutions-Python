if __name__ == '__main__':
    input_arr = []
    min_score = float("inf")
    s_min_score = float("inf")
    min_score_array = []
    s_min_score_array = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if min_score > score:
            s_min_score = min_score
            s_min_score_array = min_score_array
            min_score = score
            min_score_array = [name]
        elif min_score < score < s_min_score:
            s_min_score = score
            s_min_score_array = [name]
        elif min_score == score:
            min_score_array.append(name)
        elif s_min_score == score:
            s_min_score_array.append(name)
    s_min_score_array.sort()
    for i in s_min_score_array:
        print(i)

