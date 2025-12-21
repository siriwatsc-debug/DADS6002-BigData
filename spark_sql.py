# -*- coding: utf-8 -*-
#!/usr/bin/env python

from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType
from pyspark.sql.functions import avg

custom_schema = StructType([
    StructField("person_id", IntegerType(), True),
    StructField("district_id", IntegerType(), True),
    StructField("personal_income", FloatType(), True)
])


sc = SparkContext(appName="AverageIncomePerDistrictSQL")
sqlContext = SQLContext(sc)

file_path = "/user/cloudera/myIncome.txt" 
input_rdd = sc.textFile(file_path)

def parse_line(line):
    parts = line.split(',')
    if len(parts) == 3:
        try:
            return (int(parts[0]), int(parts[1]), float(parts[2]))
        except ValueError:
            return None
    return None

row_rdd = input_rdd.map(parse_line).filter(lambda x: x is not None)

df = sqlContext.createDataFrame(row_rdd, custom_schema)

df.registerTempTable("income_table")

result = sqlContext.sql("""
    SELECT district_id, AVG(personal_income) AS average_income
    FROM income_table
    GROUP BY district_id
    ORDER BY district_id
""")
print("--- Result from Spark SQL Query ---")
result.show() 


sc.stop()
