#target: to calculate cgpa given the input
#what input? input of course numbers
#what output: total cgpa

course_codes = [101, 102, 103, 104, 105, 106, 107, 108, 150, 199]
course_credits = [3,4,3,3,3,3,4,3,3,2]
sgpa = 0
for course in range(len(course_codes)):
    print("Please enter your course code, course credit and acquired gpa, in that order: ")
    icode, icredit, gpa = list(map(float, input().split()))
    if icode==course_codes[course]:
        sgpa+= gpa*icredit
cgpa = sgpa/sum(course_credits)
print(f"Your overall CGPA is: {cgpa}")
        
        
        
