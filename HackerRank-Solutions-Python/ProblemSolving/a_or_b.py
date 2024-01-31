#!/bin/python3

import os
import sys

#
# Complete the aOrB function below.
#
def aOrB(k, a, b, c):
    scale = 16 
    num_of_bits = max(len(a), len(b), len(c)) * 4

    A = bin(int(a, scale))[2:].zfill(num_of_bits)
    B = bin(int(b, scale))[2:].zfill(num_of_bits)
    C = bin(int(c, scale))[2:].zfill(num_of_bits)
    A = list(A)
    B = list(B)
    C = list(C)

    for i in range(num_of_bits):
        if C[i] == '0':
            if A[i] == '1':
                A[i] = '0'
                k -= 1
            if B[i] == '1':
                B[i] = '0'
                k -= 1
        else:
            if A[i] == '0' and B[i] == '0':
                B[i] = '1'
                k -= 1                

    if k < 0:
        print(-1)
        return
                
    for i in range(num_of_bits):
        if k == 0:
            break
        else:
            if C[i] == '1' and A[i] == '1':
                if k > 1 and B[i] == '0':
                     A[i] = '0'
                     B[i] = '1'
                     k -= 2
                     
                elif B[i] == '1':
                    A[i] = '0'
                    k -= 1
                 
    A = hex(int(''.join(A), 2))[2:].upper()
    B = hex(int(''.join(B), 2))[2:].upper()
    print(A)
    print(B)
    return
                
                

if __name__ == '__main__':
    # q = int(input())

    # for q_itr in range(q):
    k = 3
    a = '81B9BB94E'
    b = '8AB3CA95E'
    c = '8BBBFB95E'
    aOrB(k, a, b, c)
