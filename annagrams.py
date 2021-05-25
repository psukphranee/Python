# Write your code here
#get string length
from collections import Counter
import math

s = input()
n = len(s)
counter = 0


import operator as op
from functools import reduce
def ncr(n, r):
    if(r > n):
        return 0
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

#loop through substring of length k, 1 <= k <= n
for k in range(1,n+1):
    substrings = []
    #iterate through starting indices k_1, 0 <= k_i <= n-k.
    for k_i in range(n-k + 1):
        #append sorted substrings of all possible lengths whose starting index is k_i
        substrings.append(''.join(sorted(s[k_i:k_i + k])))
    
    #count the number of occurances of each
    substringsCounter = Counter(substrings)
    #loop through the Counter's values, x, and add to counter xChoose2 
    for x in substringsCounter.values():
        counter += ncr(x, 2)


    print(substrings)
    print(substringsCounter)
    print('----------------')

print(counter)
#substrings are of length k, 1<= k <= n
#iterate through these possible sizes`