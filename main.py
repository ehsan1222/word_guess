from game import *


def play(game):
    print(f"Write Your Guess Character: ")
    while True:
        alphabet = input(f"(Remaining Life: {show_life(game)}) Enter a guess ({game['masked_word']}) : ")
        try:
            guess(game, alphabet)
        except IllegalWordException as exp:
            print(f"Please write a Alphabetic Word")
            continue
        except GameLossException as exp:
            print(f"You are loss. Actual word is ({game['actual_word']})")
            break
        except GameWonException as exp:
            print(f"Oh YES..... You Won!! :)")
            break


def show_life(game):
    return "|" * game["number_of_suggest"]


if __name__ == "__main__":
    game = start_game()
    play(game)
