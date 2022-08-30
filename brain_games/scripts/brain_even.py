#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.cli import *


def brain_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    i = 1
    while i <= 3:
        num = randint(0, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if answer == 'yes' and num % 2 == 0 and i <= 2:
            print('correct')
            i += 1
        elif answer == 'no' and num % 2 != 0 and i <= 2:
            print('correct')
            i += 1
        elif answer == 'yes' and num % 2 == 0 and i == 3:
            print(f'Congratilation, {name}!')
            i +=3
        elif (answer == 'no' or answer != 'y') and num % 2 != 0 and i == 3:
            print(f'Congratilation, {name}!')
            i +=3
        else:
            if answer != 'no' and num % 2 != 0:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                i +=3
            elif answer != 'yes' and num % 2 == 0:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
                i +=3
            print(f"Let's try again, {name}!")

def main():
    brain_even()

if __name__ == '__main__':
    main()
