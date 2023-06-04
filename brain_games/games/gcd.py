from random import choices
from brain_games.flow import flow_game

QUIZ = "Find the greatest common divisor of given numbers."


def get_gcd(num1, num2):
    min_num, max_num = min(num1, num2), max(num1, num2)
    divisor = min_num
    while divisor > 0:
        if max_num % divisor == 0 and min_num % divisor == 0:
            return divisor
        divisor -= 1


def get_quiz():
    print(QUIZ)
    num1, num2 = choices(range(1, 30), k=2)
    question = f"{num1} {num2}"
    answer = get_gcd(num1, num2)
    return question, str(answer)


def run_game():
    flow_game(get_quiz)
