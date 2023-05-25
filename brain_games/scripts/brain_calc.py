from random import choice
from random import randint


def main():

    def correct_1():
        print('correct!')
        number = randint(0, 10)
        number_1 = randint(0, 10)
        arithmetic = ['+', '-', '*', '/']
        arithm = choice(arithmetic)
        if arithm == '+':
            print(f'Question: {number} + {number_1}')
            result = number + number_1
        if arithm == '-':
            print(f'Question: {number} - {number_1}')
            result = number - number_1
        if arithm == '*':
            print(f'Question: {number} * {number_1}')
            result = number * number_1
        answer = int(input('Your answer: '))
        if answer == result:
            print(f'Correct! \nCongratulations, {name}!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}."
                  f"\nLet's try again, {name}!")

    def correct():
        print('correct!')
        number = randint(0, 10)
        number_1 = randint(0, 10)
        arithmetic = ['+', '-', '*', '/']
        arithm = choice(arithmetic)
        if arithm == '+':
            print(f'Question: {number} + {number_1}')
            result = number + number_1
        if arithm == '-':
            print(f'Question: {number} - {number_1}')
            result = number - number_1
        if arithm == '*':
            print(f'Question: {number} * {number_1}')
            result = number * number_1
        answer = int(input('Your answer: '))
        if answer == result:
            return correct_1()
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}."
                  f"\nLet's try again, {name}!")
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    number = randint(0, 10)
    number_1 = randint(0, 10)
    arithmetic = ['+', '-', '*', '/']
    arithm = choice(arithmetic)
    if arithm == '+':
        print(f'Question: {number} + {number_1}')
        result = number + number_1
    if arithm == '-':
        print(f'Question: {number} - {number_1}')
        result = number - number_1
    if arithm == '*':
        print(f'Question: {number} * {number_1}')
        result = number * number_1
    answer = int(input('Your answer: '))
    if answer == result:
        return correct()
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {result}."
              f"\nLet's try again, {name}!")
