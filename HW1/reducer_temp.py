#!/usr/bin/env python3

# This reducer script calculates and outputs the average temperature for each city 
# (city name with its average temperature) from the mapper output.

import sys

############ TODO: YOUR CODE HERE #########

cur_city = None
cur_temp_sum = 0
cur_temp_count = 0

for line in sys.stdin:
    city, temp = line.split('\t')
    
    temp = float(temp)
    
    if city != cur_city:
        if cur_city is not None:
            print(f'{cur_city}\t{cur_temp_sum/cur_temp_count}')
        
        cur_city = city
        cur_temp_count = 0
        cur_temp_sum = 0

    cur_temp_count += 1
    cur_temp_sum += temp

if cur_city is not None:
    print(f'{cur_city}\t{cur_temp_sum/cur_temp_count}')


############ (END) YOUR CODE ##############
