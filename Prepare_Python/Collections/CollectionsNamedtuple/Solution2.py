import sys
from collections import namedtuple

input_values = sys.stdin.read().splitlines()

columns = input_values[1].split()
# print(columns)

col_name_index = {col: idx for idx, col in enumerate(columns)}

# print(col_name_index)

Stu_record = namedtuple("Stu_record", columns)
stu_marks = 0

for rec in input_values[2:]:
    rec_list = rec.split()
    student_details = Stu_record(*rec_list)
    stu_marks += int(student_details.MARKS)
    
print(f"{(stu_marks/ float(input_values[0])):.2f}")