from random import randint


#GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, ' + name + '!')
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_number = randint(1, 20)
        print('Question: ', random_number)
        answer = input('Your answer: ')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer != correct_answer:
            print(answer + " is wrong answer ;(. Correct answer was " + correct_answer + ".")
            return f"Let's try again, " + name
        else:
            print('Correct!')
    return f'Congratulations, ' + name + '!'
