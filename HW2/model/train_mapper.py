#!/usr/bin/env python
"""
Mapper reads in text documents and emits word counts by class.
INPUT:                                                    
    DocID \t true_class \t subject \t body                
OUTPUT:                                                   
    word \t class0_partialCount,class1_partialCount       
    

Instructions:
 
    A few reminders:
    1) You can use the following tokenizing method:
         words = re.findall(r'[a-z]+', text-to-tokenize.lower())
         
    2) Don't forget to handle the various "totals" that you need
       for your conditional probabilities and class priors.
    
       
"""

import re                                                   
import sys                                                  
import numpy as np      

from operator import itemgetter
import os

#################### YOUR CODE HERE ###################
output = {}
output['#totals'] = [0,0]
output['ClassPriors'] = [0,0]

for line in sys.stdin:
    # parse input and tokenize
    docID, _class, subject, body = line.lower().strip().split('\t')
    words = re.findall(r'[a-z]+', subject + ' ' + body) 

    _class = int(_class)

    output['ClassPriors'][_class] += 1
    
    for word in words:
        if word not in output:
            output[word] = [0, 0]
        
        output[word][_class] += 1
        output['#totals'][_class] += 1

for word, counts in output.items():
    print(f'{word}\t{counts[0]},{counts[1]}')
    
#################### (END) YOUR CODE ###################