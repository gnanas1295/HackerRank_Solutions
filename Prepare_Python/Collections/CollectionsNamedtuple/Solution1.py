# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from collections import namedtuple

student_details = sys.stdin.read().splitlines()

# print(student_details)

student_list_field_names = student_details[1].split()
# print(student_list_field_names)
student_list_field_names_index = [0,0,0,0]
for idx in range(4):
     # print(student_list_field_names[idx])
    if student_list_field_names[idx] == "ID":
        student_list_field_names_index[0] = idx
    if student_list_field_names[idx] == "MARKS":
        student_list_field_names_index[1] = idx
    if student_list_field_names[idx] == "NAME":
        student_list_field_names_index[2] = idx
    if student_list_field_names[idx] == "CLASS":
        student_list_field_names_index[3] = idx


# print(student_list_field_names_index)
student_details_tuple = namedtuple('student_details_tuple','ID MARKS NAME CLASS')

stu_marks = 0
for idx in range(2, (int(student_details[0])+2)):
    temp = student_details[idx].split()
    ID = temp[student_list_field_names_index[0]]
    MARKS = temp[student_list_field_names_index[1]]
    NAME = temp[student_list_field_names_index[2]]
    CLASS = temp[student_list_field_names_index[3]]
    stu_marks += int(MARKS)
    student_details_tuple_final = student_details_tuple(ID = int(ID), MARKS = int(MARKS), NAME = NAME, CLASS=CLASS)

# print(stu_marks)
average = stu_marks / int(student_details[0])

print(average)