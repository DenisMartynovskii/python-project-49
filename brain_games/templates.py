import prompt


def flow_game(get_result, case):
    print("Welcome to the Brain Games!")
    print(case, end="\n\n")
    user_name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(user_name))
    tries = 3
    for i in range(tries):
        question, answer = get_result()
        print('Question: {}'.format(question))
        user_ask = input("Your answer: ")
        if answer == user_ask:
            print("Correct!")
        else:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                    user_ask, answer
                )
            )
            print("Let's try again, {}!".format(user_name))
            break
    else:
        print("Congratulations, {}!".format(user_name))
