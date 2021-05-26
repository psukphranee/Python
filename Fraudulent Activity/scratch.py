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

'''
###### dict approach
dte = dict()
for i in range(d):
    dte[i] = expenditure[i]

mid_0 = math.ceil(d/2) - 1
mid_len = 2 if (d%2 == 0) else 1
mid = sorted(dte.values())[mid_0: mid_0 + mid_len]
limit = 2*median(mid)
count = 0

start = time.time()
print(start)

for i in range(d, N):
    nxt = expenditure[i] #next expediture
    if(nxt >= limit): #is it above limit
        count += 1
    #update dte
    for j in range(d-1):
        dte[j] = dte[j+1]
    dte[d] = nxt
    mid = sorted(dte.values())[mid_0: mid_0 + mid_len]
    limit = 2*median(mid)
    print("%d/%d" % (i, N), end='\r')
end = time.time() 
print("\n%d" % (end-start))


'''
#################################Optimize 1

#we'll need a matrix of 3 indices to keep track of the past d expenditures:
#the expenditure value, days till not counted,
#and whether its a median number(s) or left/right of it.

#we start by populating a buffer of d number of expenditures.
#we then enumerate them to keep track of days to expiry.
#next we sort the tuple by its expense value. this way we can use indexing to
#calculate the median value.  
buffer = expenditure[:d]
buffer_tagged = list(enumerate(buffer))
buffer_tagged_srt = sorted(buffer_tagged, key=lambda x : x[1])

#for odd length, the median value is the middle number, otherwise the average of the 
#two middle numbers. mid_0 gets the index of either the median or the first number median.
mid_0 = math.ceil(d/2) - 1
mid_len = 2 if (d%2 == 0) else 1
#tracker will be the dX3 table that keeps track of our expenditures
tracker = [[0]*d for _ in range(3)]
tracker[0] = [item[0] for item in buffer_tagged_srt]
tracker[1] = [item[1] for item in buffer_tagged_srt]
tracker[2][:mid_0] = ['L']*mid_0
tracker[2][mid_0:] = ['R']*(d-mid_0)
#tracker[2][mid_0:mid_0 + mid_len] = ['M']*mid_len
#tracker[2][mid_0+mid_len:] = ['R']*(d-mid_0-mid_len)

#tracker[0] : expiry
#tracker[1] : value
#tracker[2] : L, M, R


count = 0
#Our stage is now set up to accept incoming expenditures. 
start = time.time()
for i in range(d, n):
    #determine which number is to be popped off.

    #get next expenditure
    nxt = expenditure[i]

    #determine if its beyond the limit
    limit = 2*median(tracker[1][mid_0:mid_0 + mid_len])
    if(nxt >= limit):
        count +=1

    #determine what expenditure is next expired and pop it
    i_exp = tracker[0].index(0)
    tracker[0].pop(i_exp)
    tracker[1].pop(i_exp)
    
    #update expiry values
    tracker[0] = [i-1 for i in tracker[0]]
    #print('pop index', i_exp )
    #find place to insert nxt
    try:
        for j in reversed(range(d-1)):
            if(nxt >= tracker[1][j]):
                tracker[1].insert(j, nxt)
                tracker[0].insert(j, d-1)
                #print("insert:", nxt, "into %d of %d" % (j, len(tracker[1])), " | %d, %d, %d " % (tracker[1][j-1], tracker[1][j], tracker[1][j+1]))
                break
        print("%d/%d" % (i, N), end='\r')
    except IndexError:
        print("IndexError: ", j, len(tracker[1]), len(tracker[0]))
        input()
end = time.time() 
print("\n%d" % (end-start))



'''
    #determine where expenditure will go into: left of median, into median, right of median
    if(nxt < mid[0]):
        flag_in = 'L'
    else:
        flag_in = 'R'
    
    #run replacement algorithm
    #update expiry values
    tracker[0] = [i-1 for i in tracker[0]]
    if(flag_exp == 'L'):
        if(flag_in == 'L'):
            #replace the outgoing value, set its expiry to max. this won't effect median value
            tracker[0][i_exp] = d-1
            tracker[1][i_exp] = nxt
        else: #flag_in is R
            tempVals = tracker[1][mid_0:]
            tempVals.append(nxt)
            tempExpiry = tracker[0][mid_0:]
            tempExpiry.append(d-1)
            tempSorted = sorted(zip(tempExpiry, tempVals),key=lambda x: x[1])
            #append to tracker
            tracker[0][mid_0:] = [x[0] for x in tempSorted]
            tracker[1][mid_0:] = [x[1] for x in tempSorted]
            #pop expired
            tracker[0].pop(i_exp)
            tracker[1].pop(i_exp)
    else: #flag_exp is R
        if(flag_in == 'L'):
            tracker[0].pop(i_exp)
            tracker[1].pop(i_exp)
            tracker[0].insert(0, d-1)
            tracker[1].insert(0, nxt)
            #
            tempVals = tracker[1][:mid_0+1]
            tempExpiry = tracker[0][:mid_0+1]
            tempSorted = sorted(zip(tracker, tempVals),key=lambda x: x[1])
            tracker[0][:mid_0+1] = [x[0] for x in tempSorted]
            tracker[1][:mid_0+1] = [x[1] for x in tempSorted]
        else: #flag_in=='R'
            tracker[0][i_exp] = d-1
            tracker[1][i_exp] = nxt
            tempSorted = sorted(zip(tempExpiry, tempVals),key=lambda x: x[1])
            #append to tracker
            tracker[0][mid_0:] = [x[0] for x in tempSorted]
            tracker[1][mid_0:] = [x[1] for x in tempSorted]
    
'''


################Brute Force###########
print("Brute Force")
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
