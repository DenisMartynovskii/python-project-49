from random import randint
from brain_games.templates import flow_game, greet_user


def is_even():
    random_num = randint(0, 100)
    result = "yes" if (random_num % 2 == 0) else "no"
    print("Question: ", random_num)
    return result


def run_game():
    case = 'Answer "yes" if number even otherwise answer "no".'
    name = greet_user(case)
    flow_game(is_even, name)
