#!/usr/bin/env python3

# This reducer script calculates the average salary for each department from the mapper output 

import sys


############ TODO: YOUR CODE HERE #########

cur_dept = None
cur_salary_sum = 0
cur_salary_count = 0

for line in sys.stdin:
    dept, salary = line.split('\t')
    
    salary = float(salary)
    
    if dept != cur_dept:
        if cur_dept is not None:
            print(f'{cur_dept}\t{cur_salary_sum/cur_salary_count}')
        
        cur_dept = dept
        cur_salary_count = 0
        cur_salary_sum = 0

    cur_salary_count += 1
    cur_salary_sum += salary

if cur_dept is not None:
    print(f'{cur_dept}\t{cur_salary_sum/cur_salary_count}')




############ (END) YOUR CODE ##############
