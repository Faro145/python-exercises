def near (string1, string2):

    a = len(string1)
    b = len(string2)

    if a > b:
        return True
    else:
        return False

print(near("reset", "rest"))
