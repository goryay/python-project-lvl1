from random import randint


GAME_RULES = 'What number is missing in the progression?'
MIN_START_NUMBER = 0
MAX_START_NUMBER = 100
MIN_PROGRESSION_STEP = 1
MAX_PROGRESSION_STEP = 10
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 20


def generate_progression(start, finish, step):
    progression_list = [str(n) for n in range(start, finish, step)]
    return progression_list


def make_task():
    step = randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    start = randint(MIN_START_NUMBER, MAX_START_NUMBER)
    length = randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    finish = start + step * length

    progression_list = generate_progression(start, finish, step)
    missing_item = randint(0, length - 1)
    answer = progression_list[missing_item]
    progression_list[missing_item] = '..'
    question = ' '.join(progression_list)
    return question, str(answer)
