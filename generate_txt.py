#!/usr/bin/env python3
import random

# จำนวน record ที่ต้องการ
N = 800
start_id = 1000
district_qty = 10 # สมมติว่ามี 10 เขต
start_income = 10000
end_income = 1000000
file_name = "income2.txt"
# เปิดไฟล์สำหรับเขียน
with open(file_name, "w") as f:
    for i in range(N):
        person_id = start_id + i
        district_id = random.randint(1, district_qty)   
        income = random.randint(start_income, end_income)  # รายได้สุ่มระหว่าง 10k - 1M
        f.write(f"{person_id},{district_id},{income}\n")

print(f"Generated {file_name} with {N} records")