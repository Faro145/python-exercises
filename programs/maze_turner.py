print("Maze Generator")
print("Help: # = wall, E = exit,  = passage, > = explorer")

line_one = list(input("Enter top line of maze: "))
line_two = list(input("Enter second line of maze: "))
line_three = list(input("Enter second line of maze: "))

print("Your maze:")
print(line_one, line_two, line_three, sep="\n")

line_two[1], line_two[4] = line_two[4], line_two[1]

if line_two[1] == "E":
    print("Escaped")
else:
    print("Trapped")