
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ranks = []
    scoreList = sorted(list(set(scores)), reverse=True)
    length = len(scoreList)
    index = length - 1
    for aScore in alice:
        while index >= 0 and aScore >= scoreList[index]:
            index -= 1

        ranks.append(index + 2)

    return ranks

# def climbingLeaderboard(scores, alice):
#     scores = sorted(list(set(scores)))
#     index = 0
#     rank_list = []
#     n = len(scores)
#     for i in alice:
#         while (n > index and i >= scores[index]):
#             index += 1
#         rank_list.append(n+1-index)
#     return rank_list


if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
    print(result)
