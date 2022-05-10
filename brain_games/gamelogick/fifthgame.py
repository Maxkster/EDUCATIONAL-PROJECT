#!/usr/bin/env python

def brain_prime():
    from random import randint
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    counter2 = 0
    while counter != 3:
        random_number = randint(1, 100)
        print(random_number)
        for i in range(1, random_number + 1):
            if random_number % i == 0:
                counter2 += 1
        answer=input()
        if answer=='yes' and counter2 == 2:
            counter += 1
            continue
        elif answer=='no' and counter2 != 2:
            counter += 1
            continue
        else:
            print("wrong answer ;(. Correct answer was 'yes'.\nLet's try again.")
            break
    if counter == 3:
        print('Correct')
