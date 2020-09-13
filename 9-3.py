##Solution to Think Python, Chapter 9, Exercise 3, Part 1
##Forbidden Letters

def avoids():
    c = str(input('please enter letters: '))
    b = str(input('please enter a word: '))
    for a in b:
        num = 0
        while num < len(c):
            if a == c[num]:
                return False
            num += 1
    return True

print(avoids())


