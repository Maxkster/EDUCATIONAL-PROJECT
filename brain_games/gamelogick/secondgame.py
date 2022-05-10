#!/usr/bin/env python



def brain_calc():
    counter=0
    from random import choice,randint
    print('What is the result of the expression?')
    while counter != 3:
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        operator=choice('+-*')
        print(f"Question: {random_number1}{operator}{random_number2}")
        number=eval(str(random_number1)+operator+str(random_number2))
        if number==int(input()):
            counter += 1
            continue
        else:
            print("is wrong answer ;(. Correct answer was '175'.\nLet's try again.")
            break
    if counter == 3: print('Correct!')