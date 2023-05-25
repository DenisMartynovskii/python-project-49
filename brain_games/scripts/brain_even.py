from random import randint


def main():
    def correct_1(answer):
        print('correct')
        number = randint(1, 1000)
        print(f'Question: {number}')
        answer = (input('Your answer: '))
        if number % 2 == 0 and answer == 'yes':
            print(f'Correct! \nCongratulations, {name}!')
        elif number % 2 != 0 and answer == 'no':
            print(f'Correct! \nCongratulations, {name}!')
        elif number % 2 == 0 and answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'."
                  f"\nLet's try again, {name}!")
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
                  f"\nLet's try again, {name}!")

    def correct(answer):
        print('correct')
        number = randint(1, 1000)
        print(f'Question: {number}')
        answer = (input('Your answer: '))
        if number % 2 == 0 and answer == 'yes':
            return correct_1('yes')
        elif number % 2 != 0 and answer == 'no':
            return correct_1('no')
        elif number % 2 == 0 and answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'."
                  f"\nLet's try again, {name}!")
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
                  f"\nLet's try again, {name}!")
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number = randint(1, 1000)
    print(f'Question: {number}')
    answer = (input('Your answer: '))
    if number % 2 == 0 and answer == 'yes':
        return correct('yes')
    elif number % 2 != 0 and answer == 'no':
        return correct('no')
    elif number % 2 == 0 and answer == 'no':
        print(f"'no' is wrong answer ;(. Correct answer was 'yes'."
              f"\nLet's try again, {name}!")
    else:
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
              f"\nLet's try again, {name}!")
