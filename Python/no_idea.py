# Enter your code here. Read input from STDIN. Print output to STDOUT

def no_idea(arr, A, B):
    score = 0
    for element in arr:
        if element in A:
            score += 1
        if element in B:
            score -= 1
    return score


if __name__ == '__main__':
    nm= input().rstrip().split(' ')
    arr = input().split(' ')
    A = set(input().split(' '))
    B = set(input().split(' '))
    result = no_idea(arr, A, B)
    print(result)


