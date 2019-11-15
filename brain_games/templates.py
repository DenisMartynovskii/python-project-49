import prompt


def greet_user(task_name):
    print("Welcome to the Brain Games!")
    print(task_name, end="\n\n")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    return name


def begin_game(get_result, user_name):
    successful_tries = 3
    while successful_tries > 0:
        result = get_result()
        user_ask = input("Your answer: ")
        if str(result) == user_ask:
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
