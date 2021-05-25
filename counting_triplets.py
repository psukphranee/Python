#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import product

# Complete the countTriplets function below.
def countTriplets(arr, r):
    
    b = max(arr)
    alpha = b // (r**2)
    S = set(arr)

    #print(arr)
    print(b, alpha)
    print(S)
    
    A = set([x for x in S if x <= alpha])
    B = set([r*x for x in A]).intersection(S)
    C = set([r*x for x in B]).intersection(S)
    
    A_indices = [i for i,x in enumerate(arr) if x in A]
    B_indices = [i for i,x in enumerate(arr) if x in B]
    C_indices = [i for i,x in enumerate(arr) if x in C]

    #catalog numbers and their indices
    catalog = dict()
    for num in S:
        catalog[num] = sorted([i for i,x in enumerate(arr) if x==num])
    
    total = 0
    #for all x in A, take the cartesion product of indices of x, rx, and rrx to get all possible triplets of indices
    '''
    for x in A:
        print("Gathering product for ", x)
        all_prod = product(catalog[x], catalog[r*x], catalog[r*r*x])
        #we now filter the triplets to ones with strictly increasing indices
        print('Filtering')
        filtered_prod = filter(lambda x: x[0] < x[1] < x[2], all_prod)
        #count the number of filtered_prod and add to total
        print('Counting...')
        for _ in filtered_prod:
            print('Current total ', total, end='\r')
            total += 1
        
    '''
    return total
    
    
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('input01.txt', 'r')
    
    nr = fptr.readline().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, fptr.readline().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)
    #fptr.write(str(ans) + '\n')

    #fptr.close()
