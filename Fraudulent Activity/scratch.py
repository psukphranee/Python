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

N = len(expenditure)
if(d >= n):
    print(0)
#################################Optimize 1
#create list for median value(s) and
#values to left of right of median value(s)
#initialize
buffer = expenditure[:d]
buffer_tagged = list(enumerate(buffer))
buffer_tagged_srt = sorted(buffer_tagged, key=lambda x : x[1])

#split the list of previous expenditures in to three parts. 
#the mid part will have either one or two for odd and even d, resp.
#first calculate the mid parts first index and its length {1,2}
mid_0 = math.ceil(d/2) - 1
mid_len = 2 if (d%2 == 0) else 1

mid = buffer_tagged_srt[mid_0: mid_0+mid_len]
left = buffer_tagged_srt[:mid_0]
right = buffer_tagged_srt[mid_0+mid_len:]




################Brute Force###########
if(d >= n):
    print(0)
    
#initialize queue
spent = expenditure[:d]
limit = 2*median(spent)
total = 0
#loop
start = time.time()
print(start)
for i in range(d, N):
    nxt = expenditure[i]
    if(nxt >= limit):
        total+=1
    spent.pop(0)
    spent.append(nxt)
    limit = 2*median(spent)
    print("%d/%d" % (i, N), end='\r')
end = time.time() 
print("\n%d" % (end-start))