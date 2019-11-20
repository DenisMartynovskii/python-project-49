from random import randint
from brain_games.templates import flow_game, greet_user


def is_even():
    question_digit =randint(0, 100)
    question = "Question: {}".format(question_digit)
    answer = "yes" if (question_digit % 2 == 0) else "no"
    return question, answer


def run_game():
    case = 'Answer "yes" if number even otherwise answer "no".'
    name = greet_user(case)
    flow_game(is_even, name)
