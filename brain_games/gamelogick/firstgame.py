#!/usr/bin/env python

def brain_even():
    from random import randint
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter != 3:
        random_number = randint(1, 100)
        print(f"Question: {random_number}")
        if random_number % 2 == 0:
            if input() == 'yes':
                counter += 1
                continue
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again.")
                break

        if random_number % 2 != 0:
            if input() == 'no':
                counter += 1
                continue
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again.")
                break
    if counter == 3: print('Correct!')