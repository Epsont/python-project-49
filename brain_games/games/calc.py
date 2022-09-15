#!/usr/bin/env python3
from random import randint


def brain_calc():
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    oper = randint(1, 3)
    if oper == 1:
        symbol = '+'
        correct_answer = num1 + num2
    elif oper == 2:
        symbol = '-'
        correct_answer = num1 - num2
    else:
        symbol = '*'
        correct_answer = num1 * num2
    question1 = ('What is the result of the expression?')
    question2 = (f'Question: {num1} {symbol} {num2}')
    correct_answer = str(correct_answer)
    return question1, question2, correct_answer


def main():
    brain_calc()


if __name__ == '__main__':
    main()
