count = 1

while count < 100:
    number = int(input('Please enter a number'))
    squarednumber = number ** 2
    print(number,'squared is',squarednumber)
    if squarednumber < 200:
        count + 1
    else:
        break
        
