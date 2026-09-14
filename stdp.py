name = input("Enter student name")
m_mark = int(input("Enter the mark of Maths :"))
p_mark = int(input("Enter the mark of Python :"))
e_mark = int(input("Enter the mark of English :"))
print("Student Name :",name,"\n")
print("Maths   :",m_mark)
print("Python  :",p_mark)
print("English :",e_mark)
print("\n")

total = m_mark + p_mark + e_mark
avg = total/3
if avg >= 90:
    grade = "A+"
elif avg >=80:
    grade = "A"
elif avg >=70:
    grade ="B"
elif avg >=60:
    grade = "C"
elif avg >=50:
    grade = "D"
elif avg >=40:
    grade = "E"
else:
    grade = "F"
if e_mark>=40 and p_mark>=40 and m_mark>=40:
    result ="Pass"
else:
    result = "Fail"        

if m_mark > p_mark and m_mark >e_mark:
    highest = "Maths"
elif p_mark > m_mark and p_mark >e_mark:
    highest = "Python"
else:
    highest = "English"
if highest == "Maths":
    hm = m_mark
elif highest == "Python":
    hm =p_mark
else:
    hm =e_mark

print("Total   :",total)
print("Average :",avg)
print("Grade   :",grade)
print("Result  :",result)
print("\n")
print("Highest Subject :",highest)
print("Highest Mark    :",hm)



