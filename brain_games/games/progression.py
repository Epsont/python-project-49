#!/usr/bin/env python3
from random import randint

def brain_progression():
    num1 = randint(1, 10)
    max_num_progression = 10
    num2 = num1 + max_num_progression
    list_progression = [num1, ]
    num_step = randint(1, max_num_progression - 1)
    random_index = randint(0, max_num_progression - 1)
    i = 1
    while i < max_num_progression:
        list_progression.append(list_progression[i-1] + num_step)
        #list_progression[i] = list_progression[i-1] + num_step
        i += 1
    correct_answer = str(list_progression[random_index])
    list_progression[random_index] = '..'
    question1 = (f'What number is missing in the progression?')
    #question2 = (f'Question: {list_progression}')
    question2 = 'Question:'
    i = 0
    while i < max_num_progression:
        question2 = question2 + ' ' + str(list_progression[i])
        i += 1
    return question1, question2, correct_answer

def main():
    brain_progression()

if __name__ == '__main__':
    main()

