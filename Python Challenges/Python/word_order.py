# Enter your code here. Read input from STDIN. Print output to STDOUT

def word_count(words):
    counted = {}
    for word in words:
        if word not in counted:
            counted[word] = 1
        else:
            counted[word] += 1
    res = []
    for item in counted:
        res.append(counted[item])
    length = len(res)
    res = ' '.join( str(item) for item in res )
    return length, res



if __name__ == '__main__':
    n = input()
    words = []
    for i in range(int(n)):
        words.append(input())

    length, res = word_count(words)
    print(length)
    print(res)
