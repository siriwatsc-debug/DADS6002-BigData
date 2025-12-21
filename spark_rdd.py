# -*- coding: utf-8 -*-
#!/usr/bin/env python

from pyspark import SparkContext

sc = SparkContext(appName='AverageIncomePerDistrict')
#change input path as needed
input_file = sc.textFile('/user/cloudera/myIncome.txt')


def parse_line(line):
    parts = line.split(',')
    
    district_id = int(parts[1])     
    income = float(parts[2])        
    
    return (district_id, (income, 1))

income_pairs = input_file.map(parse_line)


def combine_income(v1, v2):
   
    new_income_sum = v1[0] + v2[0]
    new_count = v1[1] + v2[1]
    return (new_income_sum, new_count)

total_income_and_count = income_pairs.reduceByKey(combine_income)

def calculate_average(total_count_tuple):
    total_income = total_count_tuple[0]
    total_count = total_count_tuple[1]
    return total_income / total_count

average_income_rdd = total_income_and_count.mapValues(calculate_average)

#change output path as needed
average_income_rdd.saveAsTextFile('/user/cloudera/spark')



sc.stop()
