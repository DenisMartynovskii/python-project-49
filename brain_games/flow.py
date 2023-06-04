import prompt


def flow_game(get_quiz):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    tries_count = 3
    print("Hello, {}!".format(user_name))
    for i in range(tries_count):
        question, correct_answer = get_quiz()
        print("Question: {}".format(question))
        user_answer = input("Your answer: ")
        if correct_answer == user_answer:
            print("Correct!")
        else:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                    user_answer, correct_answer
                )
            )
            print("Let's try again, {}!".format(user_name))
            return
    print("Congratulations, {}!".format(user_name))
