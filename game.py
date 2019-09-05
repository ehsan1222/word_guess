import random

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
    word = choose_a_word()
    masked_word = create_masked_word(word)

