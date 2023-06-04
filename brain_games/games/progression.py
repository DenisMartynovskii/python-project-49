from random import randint
from brain_games.flow import flow_game

QUIZ = "What number is missing in the progression?"

progression_length = 10


def get_progression(start, step, progression_length):
    end = start + (progression_length * step)
    progression = list(range(start, end, step))
    return progression


def get_quiz():
    print(QUIZ)
    start = randint(1, 100)
    step = randint(1, 10)
    miss_item_index = randint(1, progression_length - 1)
    progression = get_progression(start, step, progression_length)
    answer = progression.pop(miss_item_index)
    progression.insert(miss_item_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, str(answer)


def run_game():
    flow_game(get_quiz)
