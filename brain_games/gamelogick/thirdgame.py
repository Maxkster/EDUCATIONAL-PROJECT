#!/usr/bin/env python
def brain_gcd():
    counter=0
    from random import choice,randint
    from math import gcd
    print('Find the greatest common divisor of given numbers.')
    while counter != 3:
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        number=gcd(random_number1,random_number2)
        print(f"Question: {random_number1} {random_number2}")
        if number==int(input()):
            counter += 1
            continue
        else:
            print("is wrong answer ;(. Correct answer was '175'.\nLet's try again.")
            break
    if counter == 3: print('Correct!')