from random import randint
import prompt


count = 3


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    for i in range(count):
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        num = randint(1, 100)
        prime = num > 1 and (
            num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
        i = 5
        d = 2
        while prime and i * i <= num:
            prime = num % i != 0
            i += d
            d = 6 - d
        print(f'Question: {num}')
        answer = (input('Your answer: '))
        if prime is True and answer == 'yes':
            print("Correct!")
        elif prime is False and answer == 'no':
            print("Correct!")
        elif prime is False and answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
                  f"\nLet's try again, {name}!")
            return
        else:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'."
                  f"\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
