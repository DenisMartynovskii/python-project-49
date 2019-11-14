import prompt

greeting = "Welcome to the Brain Games!"


def run():
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    return name
