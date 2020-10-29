import random

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
    
word = random_line('wordlist.txt')

letters = list(word)

print(word)

if len(word) == 9:
    subword_1 = ''.join(letters[0:3])
    subword_2 = ''.join(letters[3:6])
    subword_3 = ''.join(letters[6:9])
    print(subword_1)
    print(subword_2)
    print(subword_3)
else:
    print("Try Again")

