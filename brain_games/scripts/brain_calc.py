from random import randint
from random import choice
import prompt


count = 3


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    for i in range(count):
        print('What is the result of the expression?')
        number = randint(0, 10)
        number_1 = randint(0, 10)
        arithmetic = ['+', '-', '*']
        arithm = choice(arithmetic)
        if arithm == '+':
            print(f'Question: {number} {arithm} {number_1}')
            result = number + number_1
        if arithm == '-':
            print(f'Question: {number} {arithm} {number_1}')
            result = number - number_1
        if arithm == '*':
            print(f'Question: {number} {arithm} {number_1}')
            result = number * number_1
        answer = int(input('Your answer: '))
        if answer == result:
            print("Correct!")
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}."
                  f"\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
