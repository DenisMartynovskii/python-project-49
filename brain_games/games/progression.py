from random import choices
from brain_games.templates import flow_game

case = "What number is missing in the progression?"


def generate_random():
    start, step, cut = choices(range(1, 10), k=3)
    end = start + (10 * step)
    random_items = list(range(start, end, step))
    return random_items, cut - 1


def get_progression(items):
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
    sequence, cut = generate_random()
    progression, answer = get_progression((sequence, cut))
    question = "Question: {}".format(progression)
    return question, answer


def run_game():
    flow_game(get_result, case)
