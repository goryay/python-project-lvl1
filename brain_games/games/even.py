import random


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(numb):
	return numb % 2 == 0


def game_even():
	min_random_numb = 1
	max_random_numb = 10
	random_number = random.randint(min_rand_numb, max_rand_numb)
    	if is_even(random_number):
        	answer = 'yes'
    	else:
        	answer = 'no'
    	question = str(random_number)
    	return question, answer
