from random import randint
from brain_games import cli


def is_even(num):
    return "yes" if (num % 2 == 0) else "no"


def honesty_test():
    print(cli.greeting)
    print('Answer "yes" if number even otherwise answer "no".', end="\n\n")
    user_name = cli.run()
    successful_tries = 3
    while successful_tries > 0:
        random_number = randint(1, 100)
        print("Question: ", str(random_number))
        user_ask = input("Your answer: ")
        check_even = is_even(random_number)
        if check_even == user_ask:
            print("Correct!")
            successful_tries -= 1
        else:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                    user_ask, check_even
                )
            )
            print("Let's try again, {}!".format(user_name))
            break
        print("Congratulations, {}!".format(user_name))
