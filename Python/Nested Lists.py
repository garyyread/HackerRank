# Enter your code here. Read input from STDIN. Print output to STDOUT
lines_in = int(raw_input())

# Read student marks in
records = list()
phys_marks = list()
for i in range(0,lines_in):
    name = raw_input()
    mark = float(raw_input())
    records.append([name,mark])
    phys_marks.append(mark)

# Get all students with the 2nd lowest mark
phys_marks.sort()
target_mark = phys_marks[phys_marks.__len__() - (phys_marks.__len__() - 1)]

student_with_target_mark = list()
for i in range(0,phys_marks.__len__()):
    if records[i][1] == target_mark:
        student_with_target_mark.append(records[i][0])

student_with_target_mark.sort()
for i in range(0, student_with_target_mark.__len__()):
    print student_with_target_mark[i]