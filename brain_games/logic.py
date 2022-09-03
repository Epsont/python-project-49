#!/usr/bin/env python3
import prompt

def logic(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    i = 1
    while i <= 3:
        question1, question2, correct_answer = game()
        print(question1)
        print(question2)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratilation, {name}!')

def main():
    logic()

if __name__ == '__main__':
    main()


        