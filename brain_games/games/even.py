from random import randint


QUIZ = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_quiz():
    print(QUIZ)
    question = randint(0, 100)
    answer = "yes" if is_even(question) else "no"
    return question, answer
