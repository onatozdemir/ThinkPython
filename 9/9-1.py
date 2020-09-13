## Solution for Think Python Chapter 9, Exercise 1
## Words with more than 20 characters

fin = open('words.txt')
line = fin.readline()


for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)
