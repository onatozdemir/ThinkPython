##Solution to Think Python, Chapter 9, Exercise 3
##Forbidden Letters

def avoids():
    c = str(input('please enter a letter: '))
    b = str(input('please enter a word: '))
    for a in b:
        if a == c:
            return False
    return True

print(avoids())


