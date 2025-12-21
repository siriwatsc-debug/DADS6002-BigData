#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    if len(parts) != 3:
        continue
    person_id, district_id, income = parts
    try:
        income = float(income)
        print "%s\t%s" % (district_id, income)
    except:
        continue