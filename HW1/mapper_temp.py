#!/usr/bin/env python

# This script processes input lines containing city names and temperatures, outputting each city and its corresponding temperature.

import sys

for line in sys.stdin:
    line = line.strip()
    city, temp = line.split(',')

############ TODO: YOUR CODE HERE #########
    print(f'{city}\t{temp}')




############ (END) YOUR CODE ##############
