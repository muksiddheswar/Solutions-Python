#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    length = len(arr)
    sum = 0
    largest = None
    for rowIndex in range(length -2):
        for colIndex in range(length -2):
            sum = arr[rowIndex][colIndex] + arr[rowIndex][colIndex + 1] + arr[rowIndex][colIndex + 2] + arr[rowIndex + 1][colIndex + 1] + arr[rowIndex + 2][colIndex] + arr[rowIndex + 2][colIndex + 1] + arr[rowIndex + 2][colIndex + 2]
            if sum > largest or largest == None:
                largest = sum
    return largest

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)