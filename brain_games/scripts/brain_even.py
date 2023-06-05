from brain_games.flow import flow_game
from brain_games.games.even import get_quiz


def main():
    flow_game(get_quiz)


if __name__ == "__name__":
    main()
