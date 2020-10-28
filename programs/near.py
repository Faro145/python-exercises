def near (string1, string2):
    list_string1 = list(string1)
    list_string2 = list(string2)
    for index in range(len(list_string1)):
        item_to_remove = list_string1[index]
        del list_string1[index]
        if list_string1 == list_string2:
            return True
        list_string1.insert(index, item_to_remove)
    return False
    
word1 = input("Enter First Word: ")
word2 = input("Enter Second Word: ")

print(near(word1, word2))
