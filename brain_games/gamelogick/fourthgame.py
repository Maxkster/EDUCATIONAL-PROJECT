#!/usr/bin/env python

def brain_progression():
    counter=0
    from random import choice,randint
    print('What number is missing in the progression?')
    counter=0
    while counter!=3:
        range_of_progression = randint(5, 10)
        range_of_step = randint(1, 5)
        first_number=randint(1, 100)
        list_of_numbers=[]
        for i in range(range_of_progression):
            first_number+=range_of_step
            list_of_numbers.append(first_number)
        choosen_index=choice(list(range(range_of_progression)))
        number=list_of_numbers[choosen_index]
        list_of_numbers[choosen_index]='..'
        print(*list_of_numbers)
        if int(input())==number:
            counter+=1
            continue
        else:
            counter=0
            print('Uncorrect(')
            continue
    print('Correct!')
print(brain_progression())
