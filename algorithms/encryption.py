#!/bin/python3

import math


# import os
# import random
# import re
# import sys


# Complete the encryption function below.
def encryption(s):
    length = len(s)
    low, high = math.floor(length ** 0.5), math.ceil(length ** 0.5)
    print(low, high)
    output = []
    for i in range(low):
        if len(s) >= high:
            output.append(s[:high])
            s = s[high:]
        else:
            output.append(s)
    final_list = []

    for i in range(high):
        t = ''
        for j in range(low):
            if len(output[j]) >= i + 1:
                t += output[j][i]
        final_list.append(t)
    print(output)
    print(final_list)
    return ' '.join(final_list)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = encryption(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()
