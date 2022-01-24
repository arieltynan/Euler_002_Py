# Euler Problem 002
# Solved January 2021

#Even Fibonacci numbers

import math

total = 0
numb1 = 1 #first val added
numb2 = 1 #second val added
numb3 = 0 #sum
while numb3 < 4000000: #fibonacci loop
    numb3 = numb1 + numb2
    if numb3 < 4000000:
        numb2 = numb1 #swap
        numb1 = numb3 #swap

        if numb3 % 2 == 0:
            total = total + numb3
print(total)