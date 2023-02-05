#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):

    total_difference = 0

    time1 = t1.split()
    time2 = t2.split()

    # Equalise Year
    y1 = time1[3]
    y2 = time2[3]

    year_difference = abs(y1 - y2)
    total_difference =


    # Equalise Month
    # Equalise Day
    # Equalise hour -1

    # Add Minutes
    # Add Seconds
    pass


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)

        print(delta)
