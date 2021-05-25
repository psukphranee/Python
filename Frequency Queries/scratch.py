#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

fptr = open("input10.txt")
f = fptr.readline()
q = int(f.strip())

queries = []

for _ in range(q):
    queries.append(list(map(int, fptr.readline().rstrip().split())))
fptr.close()

fptr = open("output10.txt")
f = fptr.readline()
q = int(f.strip())
RESULT = list(map(lambda x : int(x), fptr.read().rstrip().split()))
fptr.close()



##
catalog = Counter()
freq_tracker = Counter()
result = list()

for query in queries:
    if(query[0] == 1):
        freq_tracker[catalog[query[1]]] -=1
        catalog[query[1]] += 1
        freq_tracker[catalog[query[1]]] +=1
    elif(query[0] == 2):
        if(catalog[query[1]] > 0):
            freq_tracker[catalog[query[1]]] -=1
            catalog[query[1]] -= 1
            freq_tracker[catalog[query[1]]] +=1
    else:
        if(freq_tracker[query[1]] > 0):
            result.append(1)
        else:
            result.append(0)
#       
for query in queries:
    op = query[0]
    arg = query[1]
    if(op==1 or op==2):
        pm = 1 if op==1 else -1
        oldArgCt = catalog.get(arg, 0)
        newArgCt = (oldArgCt + pm) if (oldArgCt + pm) >=0 else 0
        #update catalog of counts
        catalog[arg] = newArgCt
        #get count_tracker values
        rmFrom = count_tracker.get(oldArgCt, 0)
        addTo = count_tracker.get(newArgCt, 0)
        #update count_tracker values
        rmFromNew = (rmFrom - 1) if (rmFrom - 1) >=0 else 0
        addToNew = addTo + 1
        count_tracker[rmFrom] = rmFromNew
        count_tracker[addTo] = addToNew
        #print(op)
    if(op == 3):
        if(0 in count_tracker):
            count_tracker.pop(0)
        val = count_tracker.get(arg, 0)
        #0 out negative numbers
        if(val >= 1):
            val = 1
        else:
            val = 0
        result.append(val)




    catalog[argVal] = argValCtNew
    count_tracker[argValCtNew] = count_tracker.get(argValCtNew, 0) + 1
    count_tracker[argValCtOld] = count_tracker.get(argValCtOld, 0) - 1
#debug
i = 0
for query in queries:
    op = query[0]
    argVal = query[1]  
    argValCtOld = catalog.get(argVal, 0)
    argValCtNew = 
    if(op == 1):
        argValCtNew = argValCtOld + 1
    if(op == 2):
        argValCtNew = (argValCtOld - 1 if argValCtOld >= 1 else 0)
    if(op == 3):
        val = count_tracker.get(argVal, 0)
        #0 out negative numbers
        if(val >= 1):
            val = 1
        else:
            val = 0
        result.append(val)
        #debug
        if( RESULT[i] != val):
            break
        i += 1
    
    catalog[argVal] = argValCtNew
    count_tracker[argValCtNew] = count_tracker.get(argValCtNew, 0) + 1
    count_tracker[argValCtOld] = count_tracker.get(argValCtOld, 0) - 1

query3 = [pair for pair in queries if pair[0] == 3]