from random import choices
from brain_games.flow import flow_game

case = "What number is missing in the progression?"
length = 10


def generate_sequence_items():
    start, step, cut = choices(range(1, length), k=3)
    end = start + (length * step)
    sequence = list(range(start, end, step))
    return sequence, cut - 1


def get_progression_items(sequence, cut):
    correct_answer = sequence.pop(cut)
    sequence.insert(cut, "..")
    progression = " ".join([str(i) for i in sequence])
    return progression, correct_answer


def get_quiz():
    sequence, cut = generate_sequence_items()
    question, answer = get_progression_items(sequence, cut)
    return question, str(answer)


def run_game():
    flow_game(get_quiz, case)
