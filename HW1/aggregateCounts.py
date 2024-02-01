#!/usr/bin/env python
"""
This script reads word counts from STDIN and aggregates
the counts for any duplicated words.

INPUT & OUTPUT FORMAT:
    word \t count
USAGE:
    python aggregateCounts.py < yourCountsFile.txt

"""

# imports
import sys
from collections import defaultdict

counts = defaultdict(int)
# stream over lines from Standard Input
for line in sys.stdin:
    word, count  = line.split()
    counts[word] += int(count)
for wrd, count in counts.items():
    print("{}\t{}".format(wrd,count))
    
