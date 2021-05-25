import math
import os
import random
import re
import sys
from statistics import median
import time

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
buffer_tagged = list(zip(buffer, range(len(buffer))))
med = []
left = []
right = []

if(N % 2 == 0): #if n is even:
    med = []


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