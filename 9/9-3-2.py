##Solution for Think Python Chapter 9, Exercise 3, Part 2
fin = open('words.txt')
line = fin.readline()


def avoids(letters, word):
    b = word
    for a in b:
        num = 0
        while num < len(letters):
            if a == letters[num]:
                return False
            num +=1
    return True

def list_of_avois():
    count = 0
    letters = str(input('please enter letters: '))
    for line in fin:
        word = line.strip()
        if avoids(letters, word) == True:
            count += 1
        else:
            count = count
    return count

print(list_of_avois())



        





