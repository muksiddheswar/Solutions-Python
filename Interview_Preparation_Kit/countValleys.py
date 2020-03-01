#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    primary = None
    secondary = []
    hill = 0
    valley = 0
    for step in s:
        if primary is None:
            primary = step

        elif len(secondary) == 0 and step == primary:
            secondary.append(step)

        elif len(secondary) == 0 and step != primary:
            if primary == 'U':
                hill += 1
            else:
                valley += 1

            primary = None

        elif len(secondary) > 0:
            last_item = secondary[len(secondary) - 1]
            if last_item == step:
                secondary.append(step)
            else:
                secondary.pop()
    return valley


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)