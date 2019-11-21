from random import randrange
from brain_games.templates import flow_game

case = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    index = num
    count = 0
    while index > 0:
        if num % index == 0:
            count += 1
        index -= 1
    return True if count == 2 else False


def get_result():
    random_num = randrange(1, 60, 2)
    answer = "yes" if is_prime(random_num) else "no"
    question = "Question: {}".format(random_num)
    return question, answer


def run_game():
    flow_game(get_result, case)
