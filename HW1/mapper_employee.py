#!/usr/bin/env python

# This mapper script processes each line of input to extract department and salary information, then outputs these as a key-value pair.

import sys

############ TODO: YOUR CODE HERE #########



for line in sys.stdin:
    line = line.strip()
    name, dept, salary = line.split(',')

    print(f'{dept}\t{salary}')



############ (END) YOUR CODE ##############