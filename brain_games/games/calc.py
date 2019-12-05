from random import choice, choices
from brain_games.flow import flow_game

case = "What is the result of the expression?"

sign = choice(["+", "-", "*"])


def calculated_expression(num_1, num_2, sign):
    if sign == "+":
        result = num_1 + num_2
    elif sign == "-":
        result = num_1 - num_2
    elif sign == "*":
        result = num_1 * num_2
    return result


def get_quiz():
    num1, num2 = choices(range(1, 30), k=2)
    answer = calculated_expression(num1, num2, sign)
    question = "{} {} {}".format(num1, sign, num2)
    return question, str(answer)


def run_game():
    flow_game(get_quiz, case)
