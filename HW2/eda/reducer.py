#!/usr/bin/env python
"""
Reducer takes words with their class and partial counts and computes totals.
INPUT:
    word \t class \t partialCount 
OUTPUT:
    word \t class \t totalCount  
"""
import re
import sys

# initialize trackers
current_word = None
spam_count, ham_count = 0,0

# read from standard input
for line in sys.stdin:
    # parse input
    word, is_spam, count = line.split('\t')
    
############ YOUR CODE HERE #########
    count = int(count)
    is_spam = int(is_spam)
    
    if current_word is None:
        current_word = word
        if is_spam == 1:
            spam_count = 1
        else:
            ham_count = 1
            
    elif current_word == word:
        if is_spam == 1:
            spam_count += 1
        else:
            ham_count += 1
    
    else:
        if spam_count > 0:
            print(f'{current_word}\t1\t{spam_count}')
        if ham_count > 0:
            print(f'{current_word}\t0\t{ham_count}') 
        current_word = word
        if is_spam == 0:
            ham_count, spam_count = 1, 0
        else:
            ham_count, spam_count = 0, 1

if spam_count > 0:
            print(f'{current_word}\t1\t{spam_count}')
if ham_count > 0:
            print(f'{current_word}\t0\t{ham_count}') 

############ (END) YOUR CODE #########