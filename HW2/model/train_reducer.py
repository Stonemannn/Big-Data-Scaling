#!/usr/bin/env python
"""
Reducer aggregates word counts by class and emits frequencies.

INPUT:                                                     
    word \t class0_partialCount,class1_partialCount  
OUTPUT:
    word \t ham_count,spam_count,P(word|ham),P(word|spam)
    
Instructions:
    You are free to design a solution however you see 
    fit as long as your final model meets our required format.
    Please comment your code clearly and concisely.
    
    Tip: don't forget to emit Class Priors.
"""

##################### YOUR CODE HERE ####################
                                               
import sys                           
import os
import numpy as np


cur_word = None
cur_count = np.array([0, 0])
doc_count = np.array([0, 0])
total = np.array([0, 0])

for line in sys.stdin:
    word, count = line.split('\t')
    count_0, count_1 = count.split(',')
    count = np.array((int(count_0), int(count_1)))
    
    if word == '#totals':
        total += count

    elif word == 'ClassPriors':
        doc_count += count
    
    elif cur_word == word:
        cur_count += count
        
    else:
        if cur_word is not None:
            p = np.round(cur_count/total,3)
            print(f'{cur_word}\t{cur_count[0]},{cur_count[1]},{p[0]},{p[1]}')
        cur_word = word
        cur_count = count

        
p = np.round(cur_count/total,3)
print(f'{word}\t{cur_count[0]},{cur_count[1]},{p[0]},{p[1]}')

p = np.round(doc_count/np.sum(doc_count),3)
print(f'ClassPriors\t{doc_count[0]},{doc_count[1]},{p[0]},{p[1]}')





##################### (END) CODE HERE ####################