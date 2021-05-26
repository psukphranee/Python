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
d = d -1
N = len(expenditure)
if(d >= n):
    print(0)

tracker = expenditure[:d]

#impelement counting sort
##gather counts
tracker_cts = dict()
for i in tracker:
    tracker_cts[i] = tracker_cts.get(i, 0) + 1
##cummalitve sum
sorted_keys = sorted(tracker_cts.keys()) #range non-inclusive so no need to shift left by 1
for i in range(1,len(sorted_keys)):
    tracker_cts[sorted_keys[i]] += tracker_cts[sorted_keys[i-1]]
##created sorted list
srt_list = []
prev = 0
delta = 0
for i in range(len(sorted_keys)):
    delta = tracker_cts[sorted_keys[i]] - prev
    for j in range(delta):
        srt_list.append(sorted_keys[i])
    prev = tracker_cts[sorted_keys[i]]

#for odd length, the median value is the middle number, otherwise the average of the 
#two middle numbers. mid_0 gets the index of either the median or the first number median.
mid_0 = math.ceil(d/2) - 1
mid_len = 2 if (d%2 == 0) else 1
count = 0
start = time.time()
#loop through expenditures

for i_nxt in range(d, N):
    nxtVal = expenditure[i_nxt]
    
    #find median value(s)
    ##we know the median indices from calculation to be [mid_0, mid_0 + mid_len)
    tracker_inv = {v: k for k,v in tracker_cts.items()}
    mid_indices =  [x for x in tracker_inv.keys() if  x < (mid_0 + mid_len) and x+tracker_inv[x] >= mid_0]  
    mid_vals = [tracker_inv[y] for y in mid_indices]
    ##calculate median and limit
    limit = 2*median(mid_vals)
    print(mid_indices, " Median: %.1f, Limit: %d" % (limit/2, limit) )
    if(nxtVal >= limit):
        count += 1

    #pop and append, FIFO 
    popped = tracker.pop(0)
    tracker.append(nxtVal)
    #update tracker_cts by decrement values >= popped
    j_nxt = sorted_keys.index(popped)
    for j in range(j_nxt, len(sorted_keys)):
        tracker_cts[sorted_keys[j]] -= 1
    #increment the count of the new value or insert if non-existent
    tracker_cts[nxtVal] = tracker_cts.get(nxtVal, 0) + 1
    sorted_keys = sorted(tracker_cts.keys()) ##update sorted_keys
    
    #update cummulative sum
    g = sorted_keys.index(nxtVal)
    for k in range(g+1,len(sorted_keys)):
        tracker_cts[sorted_keys[k]] += 1
    print("%d/%d" % (i_nxt, N), end='\r')


end = time.time()
print("Time:", end-start)
