from random import choice, choices
from brain_games.templates import flow_game

case = "What is the result of the expression?"

random_sign = choice(["+", "-", "*"])


def generate_expression_of_numbers():
    random_items = choices(range(1, 30), k=2)
    random_items.append(random_sign)
    return random_items


def calculated_expression(num_1, num_2, sign):
    if sign == "+":
        result = num_1 + num_2
    elif sign == "-":
        result = num_1 - num_2
    elif sign == "*":
        result = num_1 * num_2
    return result


def get_game_components():
    num_1, num_2, sign = generate_expression_of_numbers()
    answer = calculated_expression(num_1, num_2, sign)
    question = "{} {} {}".format(num_1, sign, num_2)
    return question, str(answer)


def run_game():
    flow_game(get_game_components, case)
