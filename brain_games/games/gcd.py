from random import choices
from brain_games.templates import flow_game, greet_user


def generate_random():
    random_items = choices(range(1, 30), k=2)
    return random_items


def get_expression_result(items):
    min_num, max_num = min(items), max(items)
    index = min_num
    while index > 0:
        if max_num % index == 0 and min_num % index == 0:
            return index
        index -= 1


def get_result():
    (num_1, num_2) = generate_random()
    result = get_expression_result((num_1, num_2))
    print("Question: {} {}".format(num_1, num_2))
    return result


def run_game():
    name = greet_user("Find the greatest common divisor of given numbers.")
    flow_game(get_result, name)
