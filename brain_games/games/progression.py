from random import choices
from brain_games.templates import flow_game

case = "What number is missing in the progression?"


def generate_sequence_of_numbers():
    length = 10
    start, step, cut = choices(range(1, length), k=3)
    end = start + (length * step)
    random_items = list(range(start, end, step))
    return random_items, cut - 1


def get_progression_items(sequence, cut):
    missing_element = sequence.pop(cut)
    sequence.insert(cut, "..")
    progression = " ".join([str(i) for i in sequence])
    return progression, missing_element


def get_result():
    sequence, cut = generate_sequence_of_numbers()
    question, answer = get_progression_items(sequence, cut)
    return question, str(answer)


def run_game():
    flow_game(get_result, case)
