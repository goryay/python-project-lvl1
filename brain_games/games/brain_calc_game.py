from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'
LOWER_RANGE_LIMIT = 1
UPPER_RANGE_LIMIT = 50


def get_game_data():
    first_random_number = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    second_random_number = randint(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT)
    OPERATORS = choice(('-', '+', '*'))
    question = f'{first_random_number} {OPERATORS} {second_random_number}'
    if '-' in OPERATORS:
        answer = first_random_number - second_random_number
    elif '+' in OPERATORS:
        answer = first_random_number + second_random_number
    elif '*' in OPERATORS:
        answer = first_random_number * second_random_number
    return question, str(answer)
