import prompt

tries_count = 3


def flow_game(get_quiz, case):
    print("Welcome to the Brain Games!")
    print(case, end="\n\n")
    user_name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(user_name))
    for i in range(tries_count):
        question, answer = get_quiz()
        print("Question: {}".format(question))
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
