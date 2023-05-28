from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 50


def generate_random_number():
    return randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)


def make_task():
    number = generate_random_number()
    question = number
    answer = get_correct_answer(number)
    return (question, answer)


def get_correct_answer(number):
    if number % 2 == 0:
        return "yes"
    return "no"
