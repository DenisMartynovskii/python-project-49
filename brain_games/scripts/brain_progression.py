from random import randint


def main():

    def correct_1(answer):
        print('correct!')
        progression_length = 10
        start = randint(1, 100)
        step = randint(1, 10)
        miss_item_index = randint(1, progression_length - 1)
        end = start + (progression_length * step)
        progression = list(range(start, end, step))
        result = progression.pop(miss_item_index)
        progression.insert(miss_item_index, "..")
        question = " ".join([str(i) for i in progression])
        print(question)
        answer = int(input('Your answer: '))
        if answer == result:
            print(f'Correct! \nCongratulations, {name}!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}."
                  f"\nLet's try again, {name}!")

    def correct(answer):
        print('correct!')
        progression_length = 10
        start = randint(1, 100)
        step = randint(1, 10)
        miss_item_index = randint(1, progression_length - 1)
        end = start + (progression_length * step)
        progression = list(range(start, end, step))
        result = progression.pop(miss_item_index)
        progression.insert(miss_item_index, "..")
        question = " ".join([str(i) for i in progression])
        print(question)
        answer = int(input('Your answer: '))
        if answer == result:
            return correct_1('answer')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}."
                  f"\nLet's try again, {name}!")
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    progression_length = 10
    start = randint(1, 100)
    step = randint(1, 10)
    miss_item_index = randint(1, progression_length - 1)
    end = start + (progression_length * step)
    progression = list(range(start, end, step))
    result = progression.pop(miss_item_index)
    progression.insert(miss_item_index, "..")
    question = " ".join([str(i) for i in progression])
    print(question)
    answer = int(input('Your answer: '))
    if answer == result:
        return correct('answer')
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {result}."
              f"\nLet's try again, {name}!")
