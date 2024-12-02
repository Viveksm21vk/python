def acceptMarks():
    m1 = int(input())
    m2 = int(input())
    m3=int(input())
    return [m1,m2,m3]
def calculatePercentage(m1,m2,m3):
    total_marks = m1 + m2 + m3
    per = (total_marks / 300) * 100
    print(f"Percentage = {per}")
marks_lst = acceptMarks()
print(type(marks_lst))
calculatePercentage(marks_lst[0],marks_lst[1],marks_lst[2])