import math
import os
import random
import re
import sys
from statistics import median
import time
import math

fptr = open("input01.txt")

first_multiple_input = fptr.readline().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
expenditure = list(map(int, fptr.read().rstrip().split()))


ct_srt = dict()
mid_0 = math.ceil(d/2) - 1
mid_len = 2 if (d%2 == 0) else 1
count = 0
start = time.time()

def getVal(x):
    cumm_sum = 0
    for i in range(201):
        if(i in ct_srt):
            cumm_sum += ct_srt[i]
        if(cumm_sum >= x):
            return i

for i in range(len(expenditure)-1):
    #populate count sort dictionary
    nxtVal = expenditure[i]
    if(nxtVal in ct_srt):
        ct_srt[nxtVal] += 1
    else:
        ct_srt[nxtVal] = 1
    if i >= (d-1):
        #find median element values(s)
        if(d % 2 == 0):
            med = (getVal(d//2)+getVal(d//2 + 1))/2
        else: #(d % 2 == 1):
            med = getVal(d/2)
        #calculate limit and see if nxtVal is geq
        limit = 2* med
        if(expenditure[i+1] >= limit):
            count += 1
        #remove the leading element
        ct_srt[expenditure[i-(d-1)]] -= 1
    print("%d/%d" % (i+1, n), end='\r')


end = time.time()
print("Time:", end-start)
print(count)