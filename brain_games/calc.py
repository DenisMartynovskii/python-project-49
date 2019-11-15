from random import choice, choices
import prompt


# def is_even(num):
#     return "yes" if (num % 2 == 0) else "no"


def check_number(items):
    num_1, num_2, sign = items
    if sign == "+":
        result = num_1 + num_2
    elif sign == "-":
        result = num_1 - num_2
    else:
        result = num_1 * num_2
    return result


def random_items():
    random_items = choices(range(1, 30), k=2)
    rand_sign = choice(["+", "-", "*"])
    random_items.append(rand_sign)
    return random_items


def begin_game_calc():
    (num_1, num_2, sign) = random_items()
    result = check_number((num_1, num_2, sign))
    user_name = run()
    print("Question: {} {} {}".format(num_1, sign, num_2))
    begin_game(user_name, result)
    return result


def begin_game(user_name, result):

    successful_tries = 3
    while successful_tries > 0:
        user_ask = input("Your answer: ")
        if result == user_ask:
            print("Correct!")
            successful_tries -= 1
        else:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                    user_ask, result
                )
            )
            print("Let's try again, {}!".format(user_name))
            break
    else:
        print("Congratulations, {}!".format(user_name))


def is_even(num):
    return "yes" if (num % 2 == 0) else "no"


def run():
    greeting = "Welcome to the Brain Games!"
    print(greeting)
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    return name


print(begin_game_calc())
