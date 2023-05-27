from random import randint


def main():
    def correct_1(answer):
        print('correct!')
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
            print(f'Correct! \nCongratulations, {name}!')
        elif prime is False and answer == 'no':
            print(f'Correct! \nCongratulations, {name}!')
        elif prime is False and answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
                  f"\nLet's try again, {name}!")
        else:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'."
                  f"\nLet's try again, {name}!")

    def correct(answer):
        print('correct!')
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
            return correct_1('yes')
        elif prime is False and answer == 'no':
            return correct_1('yes')
        elif prime is False and answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
                  f"\nLet's try again, {name}!")
        else:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'."
                  f"\nLet's try again, {name}!")
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')
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
        return correct('yes')
    elif prime is False and answer == 'no':
        return correct('yes')
    elif prime is False and answer == 'yes':
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
              f"\nLet's try again, {name}!")
    else:
        print(f"'no' is wrong answer ;(. Correct answer was 'yes'."
              f"\nLet's try again, {name}!")
