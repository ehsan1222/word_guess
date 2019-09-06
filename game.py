import random

from exceptions import *

LIST_OF_WORDS = [
    "apple", "banana", "iran", "java", "python", "laptop", "light", "mars", "country", "china",
    "rocket", "airplane", "superman", "america", "mexico", "dress", "machine", "westworld"
]


def choose_a_word():
    random_word = random.choice(LIST_OF_WORDS)
    return random_word


def create_masked_word(word):
    return "*" * len(word)


def start_game(number_of_suggest=3):
    actual_word = choose_a_word()
    masked_word = create_masked_word(actual_word)
    game = {
        "actual_word": actual_word.lower(),
        "masked_word": masked_word.lower(),
        "number_of_suggest": number_of_suggest
    }
    return game


def guess(game, alphabet):
    alphabet = alphabet.lower()
    if not alphabet:
        raise IllegalWordException
    if len(alphabet) > 1:
        raise IllegalWordException
    if alphabet < 'a' or alphabet > 'z':
        raise IllegalWordException
    if alphabet in game['actual_word']:
        for i in range(len(game['actual_word'])):
            if game["actual_word"][i] == alphabet:
                game["masked_word"] = alphabet
    else:
        if game["number_of_suggest"] > 1:
            print(f"Incorrect guess. You can guess it. :)\n")
            game["number_of_suggest"] -= 1
        else:
            raise GameLossException

    if game["actual_word"] == game["masked_word"]:
        raise GameWonException
