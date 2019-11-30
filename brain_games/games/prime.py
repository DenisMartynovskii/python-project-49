from random import randrange
from brain_games.templates import flow_game

case = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    index = 1
    count = 0
    while index <= num:
        if num % index == 0:
            count += 1
        index += 1
    return count == 2


def get_game_results():
    question = randrange(1, 60, 2)
    answer = "yes" if is_prime(question) else "no"
    return question, answer


def run_game():
    flow_game(get_game_results, case)
