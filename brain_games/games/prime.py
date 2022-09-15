#!/usr/bin/env python3
from random import randint


def brain_prime():
    num = randint(1, 100)
    if num == 1:
        correct_answer = 'no'
    elif num == 2 or num == 3 or num == 5 or num == 7:
        correct_answer = 'yes'
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question1 = ('Answer "yes" if given number is prime. Otherwise answer "no".')
    question2 = (f'Question: {num}')
    return question1, question2, correct_answer


def main():
    brain_prime()


if __name__ == '__main__':
    main()
