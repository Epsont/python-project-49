#!/usr/bin/env python3
from random import randint


def brain_even():
        num = randint(0, 100)
        question1 = (f'Answer "yes" if the number is even, otherwise answer "no".')
        question2 = (f'Question: {num}')
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        return question1, question2, correct_answer



def main():
    brain_even()

if __name__ == '__main__':
    main()
