from random import randint
import prompt


count = 3


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    for i in range(count):
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
        print(f'Question: {question}')
        answer = int(input('Your answer: '))
        if answer == result:
            print("Correct!")
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}."
                  f"\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
