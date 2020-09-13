##Solution for Think Python Chapter 9, Exercise 2
##Lists the words that doesn't contain 'e' and calculates the percentage


fin = open('words.txt')
line = fin.readline()
word = line.strip()
count_line = 0
count_no_e = 0

def has_no_e(b):
    for letter in b:
        if letter == 'e' or letter == 'E':
            return False
    return True

for line in fin:
    word = line.strip()
    count_line += 1
    if has_no_e(word) == True:
        print(word)
        count_no_e += 1

print((100 / count_line)*count_no_e)
