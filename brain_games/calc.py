from random import choice, choices
from brain_games.templates import flow_game, greet_user


def generate_random():
    random_items = choices(range(1, 30), k=2)
    random_sign = choice(["+", "-", "*"])
    random_items.append(random_sign)
    return random_items


def get_expression_result(items):
    num_1, num_2, sign = items
    if sign == "+":
        result = num_1 + num_2
    elif sign == "-":
        result = num_1 - num_2
    elif sign == "*":
        result = num_1 * num_2
    return result


def get_result_calc():
    (num_1, num_2, sign) = generate_random()
    result = get_expression_result((num_1, num_2, sign))
    print("Question: {} {} {}".format(num_1, sign, num_2))
    return result


def is_even(num):
    return "yes" if (num % 2 == 0) else "no"


def run_game():
    user_name = greet_user("What is the result of the expression?")
    flow_game(get_result_calc, user_name)
