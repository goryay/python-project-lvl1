from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 50


def make_task():
    question = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer	
