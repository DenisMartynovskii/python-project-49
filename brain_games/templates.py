import prompt


def greet_user(case):
    print("Welcome to the Brain Games!")
    print(case, end="\n\n")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    return name


def flow_game(get_result, user_name):
    for tries in range(3):
        result = get_result()
        user_ask = input("Your answer: ")
        if str(result) == user_ask:
            print("Correct!")
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
