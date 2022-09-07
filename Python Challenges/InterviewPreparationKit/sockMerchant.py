
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    n_groups = {}
    for i in range(len(ar)):
        if ar[i] in n_groups:
            n_groups[ar[i]] += 1
        else:
            n_groups[ar[i]] = 1
    
    pairs = 0
    for key, item in n_groups.items():
        pairs = pairs + item//2
    return pairs


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
