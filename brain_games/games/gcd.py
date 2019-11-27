from random import choices
from brain_games.templates import flow_game

case = "Find the greatest common divisor of given numbers."


def get_gcd(items):
    min_num, max_num = min(items), max(items)
    divisor = min_num
    while divisor > 0:
        if max_num % divisor == 0 and min_num % divisor == 0:
            return divisor
        divisor -= 1


def get_result():
    question = choices(range(1, 30), k=2)
    answer = get_gcd(question)
    return question, str(answer)


def run_game():
    flow_game(get_result, case)
