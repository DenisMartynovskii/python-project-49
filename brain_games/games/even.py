from random import randint
from brain_games.templates import flow_game

case = 'Answer "yes" if number even otherwise answer "no".'


def check_even():
    question_digit = randint(0, 100)
    question = "Question: {}".format(question_digit)
    answer = "yes" if (question_digit % 2 == 0) else "no"
    return question, answer


def run_game():
    flow_game(check_even, case)
