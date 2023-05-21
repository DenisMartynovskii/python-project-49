from random import randint
from math import gcd

def main():
    def correct_1(answer):
        print ('correct!')
        number = randint(1, 100)
        number_1 = randint(1, 100)
        print(f'Question: {number} {number_1}')
        answer = int(input('Your answer: '))
        result = gcd(number, number_1)
        if answer == result: print(f'Correct! \nCongratulations, {name}!')
        else: print (f"{answer} is wrong answer ;(. Correct answer was {result}. \nLet's try again, {name}!")
    def correct(answer):
        print ('correct!')
        number = randint(1, 100)
        number_1 = randint(1, 100)
        print(f'Question: {number} {number_1}')
        answer = int(input('Your answer: '))
        result = gcd(number, number_1)
        if answer == result: return correct_1(answer)
        else: print (f"{answer} is wrong answer ;(. Correct answer was {result}. \nLet's try again, {name}!")
    print(f'Welcome to the Brain Games!')
    name =''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')
    print(f'Find the greatest common divisor of given numbers.')
    number = randint(1, 100)
    number_1 = randint(1, 100)
    print(f'Question: {number} {number_1}')
    answer = int(input('Your answer: '))
    result = gcd(number, number_1)
    if answer == result: return correct(answer)
    else: print (f"{answer} is wrong answer ;(. Correct answer was {result}. \nLet's try again, {name}!")
