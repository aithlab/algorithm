#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):    
    words = [w[-1]]
    results = 'no answer'
    for i in reversed(range(len(w)-1)):
        words.append(w[i])
        words = sorted(words, reverse=True)
        idx = max(words.index(w[i]) - 1, 0)       
        next_w = words.pop(idx)
        candi = "".join(list(w[:i]) + [next_w] + sorted(words))

        if candi > w:
            results = candi
            break
        
        words.append(next_w)
        
    return results
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
