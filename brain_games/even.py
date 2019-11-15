from random import randint
from brain_games.templates import begin_game, greet_user


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


def start_game():
    name = greet_user('Answer "yes" if number even otherwise answer "no".')
    begin_game(get_result, name)
