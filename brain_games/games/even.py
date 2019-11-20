from random import randint
from brain_games.templates import flow_game, greet_user


def is_even():
    question = randint(0, 100)
    answer = "yes" if (question % 2 == 0) else "no"
    print("Question: ", question)
    return answer


def run_game():
    case = 'Answer "yes" if number even otherwise answer "no".'
    name = greet_user(case)
    flow_game(is_even, name)
