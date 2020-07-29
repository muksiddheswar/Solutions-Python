
VOWELS = ['A', 'E', 'I', 'O', 'U']
def minion_game(string):
    vowelWords = 0
    consonantWords = 0
    length = len(string)
    for i in range(0, length):
        if string[i] in VOWELS:
            vowelWords += length - i
        else:
            consonantWords += length - i

    if vowelWords > consonantWords:
        print('Kevin %s'%vowelWords)
    elif vowelWords == consonantWords:
        print("Draw")
    else:
        print('Stuart %s'%consonantWords)


if __name__ == '__main__':
    s = input()
    minion_game(s)