#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):

    if(len(magazine) < len(note)):
        print("No")
        return

    index_table = [[0]*52 for _ in range(5)]
    word_table = [[[]]*52 for _ in range(5)]
    
    for word in magazine:
        #get ascii and length of word
        letter_index = ord(word[0]) - 65
        letter_len = len(word)-1

        print(letter_index, letter_len)
        
        #increment
        index_table[letter_len][letter_index] += 1
        word_table[letter_len][letter_index].append(word)
        
    for word in note:
        #get ascii and length of word
        letter_index = ord(word[0]) - 65
        letter_len = len(word) -1 
        
        #increment
        index_table[letter_len][letter_index] -= 1
        if(index_table[letter_len][letter_index] < 0):
            print("No")
        
        if(word in word_table[letter_len][letter_index]):
            word_table[letter_len][letter_index].remove(word)
        else:
            print("No")
            return
        
            
    print("Yes")
    
    
    
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
