if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        word_list = input().split()
        new_list = []
        for word in word_list:
            temp = word[1:] + word[0].lower() + 'ay'
            new_list.append(temp)
        f_word = new_list[0]
        f_word = f_word[0].upper() + f_word[1:]
        new_list[0] = f_word
        print(' '.join(new_list))
