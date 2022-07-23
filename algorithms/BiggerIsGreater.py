#!/bin/python3


# Complete the biggerIsGreater function below.
# def biggerIsGreater(w_in):
#     temp = list(w_in)
#     temp.sort(reverse=True)
#     temp = ''.join(temp)
#     if temp == w_in:
#         return 'no answer'
#
#
#     start = len(w_in) - 2
#     while start > -1:
#
#         if w_in[start] >= w_in[start]:
#             start -= 1
#
#         else:
#             for i in range (len(w_in) - 1, start):
#                 if



"""
    for index in range(len(w_in) - 2, -1, -1):
        suffix = w_in[index + 1:]
        l_index = unique_letters.index(w_in[index])
        if l_index < len(unique_letters) - 1:
            for u_l in unique_letters[l_index:]:
                next_number = u_l
                if next_number in suffix:
                    # swap
                    position = suffix.index(next_number)
                    temp = w_in[position + index + 1]
                    w_in[position + index + 1] = w_in[index]
                    w_in[index] = temp
                    suffix = w_in[index + 1:]
                    prefix = w_in[:index + 1]
                    suffix.sort()
                    return ''.join(prefix) + ''.join(suffix)
"""

if __name__ == '__main__':
    # T = int(input())
    # for T_itr in range(T):
    w = 'zyyxwwtrrnmlggfeb'
    # w = input()
    result = biggerIsGreater(w)
    # if T_itr == 0:
    #     print()
    print(w)
    print(result)

        # fptr.write(result + '\n')

    # fptr.close()
