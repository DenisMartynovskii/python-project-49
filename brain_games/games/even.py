from random import randint
from brain_games.templates import flow_game

case = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_quiz():
    question = randint(0, 100)
    answer = "yes" if is_even(question) else "no"
    return question, answer


def run_game():
    flow_game(get_quiz, case)
