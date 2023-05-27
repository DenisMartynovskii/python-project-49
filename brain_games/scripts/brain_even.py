from random import randint
import prompt


count = 3


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    for i in range(count):
        print('Answer "yes" if the number is even, otherwise answer "no".')
        number = randint(1, 1000)
        print(f'Question: {number}')
        answer = (input('Your answer: '))
        if number % 2 == 0 and answer == 'yes':
            print("Correct!")
        elif number % 2 != 0 and answer == 'no':
            print("Correct!")
        elif number % 2 == 0 and answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'."
                  f"\nLet's try again, {name}!")
            return
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
                  f"\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
