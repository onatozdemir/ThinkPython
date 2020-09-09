## Solution for Think Python Chpater 7, Exercise 2
## Comperation of Ramanujan's Formula for 1/pi to Python's built in function


import math

def factorial(a):
    if a == 0 :
        return 1
    else:
        return a * factorial(a-1)




def estimate_pi():
    k = 0
    result_final = 0
    pre_formula = (2 * math.sqrt(2)) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k) 
        den = factorial(k)**4 * (396)**(4*k)
        result_sum = num / den * pre_formula
        result_final += result_sum
        if abs(result_final) < 1e-15:
            break
        k += 1
        return 1 / result_final

print(estimate_pi())
        
        

        
    
