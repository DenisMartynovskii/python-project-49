from random import randint
from math import gcd
import prompt


count = 3


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    for i in range(count):
        print('Find the greatest common divisor of given numbers.')
        number = randint(1, 100)
        number_1 = randint(1, 100)
        print(f'Question: {number} {number_1}')
        answer = int(input('Your answer: '))
        result = gcd(number, number_1)
        if answer == result:
            print("Correct!")
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}."
                  f"\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
