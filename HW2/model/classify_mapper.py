#!/usr/bin/env python
"""
Mapper for Naive Bayes Inference.
INPUT:
    ID \t true_class \t subject \t body \n
OUTPUT:
    ID \t true_class \t logP(ham|doc) \t logP(spam|doc) \t predicted_class
SUPPLEMENTAL FILE: 
    This script requires a trained Naive Bayes model stored 
    as NBmodel.txt in the current directory. The model should 
    be a tab separated file whose records look like:
        WORD \t ham_count,spam_count,P(word|ham),P(word|spam)
        
Instructions:
    The supplemental file has been loaded with the log of 
    each conditional probability in the model. The code to tokenize 
    the input lines has been provided for you. Keep in mind that 
    each 'line' of this file represents a unique document 
    that we wish to classify. Fill in the missing code to get
    the probability of each class given the words in the document.
    Remember that you will need to handle the case where you
    encounter a word that is not represented in the model.
"""
import os
import re
import sys
import numpy as np

# confirm that we have access to the model file
assert 'NBmodel.txt' in os.listdir('.'), "ERROR: can't find NBmodel.txt"

# load the model into a dictionary for easy access
MODEL = {}

for record in open('NBmodel.txt', 'r').readlines():
    word, payload = record.split('\t')
    # extract conditional probabilities
    ham_cProb, spam_cProb = payload.split(',')[2:]
    # save their logs as a tuple in our model dictionary
    take_log = lambda x: np.log(x) if x != 0 else float("-inf")
    MODEL[word] = (take_log(float(ham_cProb)),
                   take_log(float(spam_cProb)))
    
# read from standard input
for line in sys.stdin:
    # parse input and tokenize
    docID, _class, subject, body = line.lower().split('\t')
    words = re.findall(r'[a-z]+', subject + ' ' + body)
    
    ################# YOUR CODE HERE ################
    # TIP: use MODEL.get(word, (0,0)) to access the tuple 
    # of log probabilities without throwing a KeyError when
    # you encounter a word that hasn't been seen by model!
    
    # initialize variables that your code should overwrite
    logpHam, logpSpam, pred_class = None, None, None
    
    logpHam, logpSpam = MODEL['ClassPriors']
    for word in words:
        logpHam += MODEL.get(word, (0,0))[0]
        logpSpam += MODEL.get(word, (0,0))[1]
    
    if logpHam > logpSpam:
        pred_class = 0
    else:
        pred_class = 1

    ################# (END) YOUR CODE ##############
    
    print("{}\t{}\t{}\t{}\t{}".format(docID, _class, logpHam, logpSpam, pred_class))