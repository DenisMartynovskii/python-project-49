from random import choice, choices
from brain_games.templates import flow_game

case = "What is the result of the expression?"


def generate_random():
    random_items = choices(range(1, 30), k=2)
    random_sign = choice(["+", "-", "*"])
    random_items.append(random_sign)
    return random_items


def sum_terms(items):
    num_1, num_2, sign = items
    if sign == "+":
        result = num_1 + num_2
    elif sign == "-":
        result = num_1 - num_2
    elif sign == "*":
        result = num_1 * num_2
    return result


def get_result():
    (num_1, num_2, sign) = generate_random()
    answer = sum_terms((num_1, num_2, sign))
    question = "Question: {} {} {}".format(num_1, sign, num_2)
    return question, answer


def run_game():
    flow_game(get_result, case)
