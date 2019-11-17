from random import choices
from brain_games.templates import flow_game, greet_user


def generate_random():
    start, step, cut = choices(range(1, 10), k=3)
    end = start + (10 * step)
    random_items = list(range(start, end, step))
    return random_items, cut -1


def get_expression_result(items):
    sequence, cut = items
    progression = ""
    for index, element in enumerate(sequence):
        if index == cut:
            result = element
            progression += " .."
        else:
            progression += " " + str(element)
    return progression, result


def get_result():
    (sequence, cut) = generate_random()
    progression, empty = get_expression_result((sequence, cut))
    print("Question:", progression)
    return empty


def run_game():
    name = greet_user("What number is missing in the progression?")
    flow_game(get_result, name)
