one = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
ten = ["", "", "", "", "", "", "", "", "", "", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", ""] 
twenty = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Twenty", "Twenty one", "Twenty two", "Twenty three", "Twenty four", "Twenty five", "Twenty six", "Twenty six", "Twenty seven", "Twenty eight", "Twenty nine"]

num = int(input("Choose number:"))

if num >= 1 and num < 10:
    word = one[int(num)]
    print(word)
elif num >= 10 and num < 20:
    word = ten[int(num)]
    print(word)
elif num >= 20 and num < 30:
    word = twenty[int(num)]
    print(word)
else:
    print("Out of range")
