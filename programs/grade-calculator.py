math = int(input("Enter maths mark:"))
chemistry = int(input("Enter chemistry mark:"))
biology =  int(input("Enter biology mark:"))

total_mark = float((math + chemistry + biology) / 300 * 100)

print("Your percentage score is", total_mark) 

if total_mark >= 70:
    print ("Your grade is A")
elif total_mark >= 60:
    print ("Your grade is B")
elif total_mark >= 50:
    print("Your grade is C")
elif total_mark >= 40:
    print("Your grade is D")
else:
    print("You failed")
