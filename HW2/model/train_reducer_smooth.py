#!/usr/bin/env python

import os
import sys                                                  
import numpy as np  

#################### YOUR CODE HERE ###################

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
            p = np.round((cur_count+1)/(total+6),3)
            print(f'{cur_word}\t{cur_count[0]},{cur_count[1]},{p[0]},{p[1]}')
        cur_word = word
        cur_count = count

        
p = np.round((cur_count+1)/(total+6),3)
print(f'{word}\t{cur_count[0]},{cur_count[1]},{p[0]},{p[1]}')

p = np.round(doc_count/np.sum(doc_count),3)
print(f'ClassPriors\t{doc_count[0]},{doc_count[1]},{p[0]},{p[1]}')



#################### (END) YOUR CODE ###################