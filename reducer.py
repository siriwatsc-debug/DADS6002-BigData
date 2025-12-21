#!/usr/bin/env python
import sys

current_district = None
total_income = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    district_id, income = parts
    try:
        income = float(income)
    except:
        continue

    if district_id == current_district:
        total_income += income
        count += 1
    else:
        if current_district is not None and count > 0:
            avg_income = total_income / count
            print "%s\t%.2f" % (current_district, avg_income)
        current_district = district_id
        total_income = income
        count = 1

if current_district is not None and count > 0:
    avg_income = total_income / count
    print "%s\t%.2f" % (current_district, avg_income)