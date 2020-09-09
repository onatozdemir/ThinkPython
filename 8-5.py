## Solution for Think Python Chapter 8, Exercise 5
## Ceaser cypher



def rotate_word(string_to_encrypt, a):
    encrypted_word = ""
    for i in string_to_encrypt:
        encrypted_word += chr(ord(i) - int(a))
    return encrypted_word

print(rotate_word(input("String to encrypt: "), input(int)))




        