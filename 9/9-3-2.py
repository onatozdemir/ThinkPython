##Solution for Think Python Chapter 9, Exercise 3, Part 2
fin = open('words.txt')
line = fin.readline()


def avoids():
    word = line.strip()
    c = str(input('please enter letters: '))
    b = word
    count = 0
    for line in fin:
        for a in b:
            num = 0
            while num < len(c):
                if a == c[num]:
                    return False
                num += 1
        count += 1
        return count

print(avoids())
        




