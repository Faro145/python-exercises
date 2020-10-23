def near (string1, string2):
    string1 = input("Enter first word")
    string2 = input("Enter second word")

    a = len(string1)
    b = len(string2)

    if a > b:
        return True
    else:
        return False
