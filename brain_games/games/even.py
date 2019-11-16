from random import randint
from brain_games.templates import flow_game, greet_user


def generate_random():
    random_item = randint(0, 100)
    return random_item


def get_expression_result(num):
    return "yes" if (num % 2 == 0) else "no"


def get_result():
    random_num = generate_random()
    result = get_expression_result(random_num)
    print("Question: ", random_num)
    return result


def run_game():
    name = greet_user('Answer "yes" if number even otherwise answer "no".')
    flow_game(get_result, name)
