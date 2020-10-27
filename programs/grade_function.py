name = input("Enter student name:")
homework = int(input("Enter homework mark out of 25:"))
assessment = int(input("Enter assessment mark out of 50:"))
final_exam = int(input("Enter final exam mark out of 100:"))

def grade(homework, assessment, final_exam):
    total_score = grade(15, 37, 68)
    return total_score

total_mark = homework + assessment + final_exam

percentage = float((total_mark/175)*100)

if percentage > 70:
    grade = "A"
elif percentage > 60:
    grade = "B"
elif percentage > 50:
    grade = "C"
elif percentage > 40:
    grade = "D"
else:
    grade = "Fail"

print(name)
print ("You scored:", percentage)
print ("Your grade is:", grade)
   

    
