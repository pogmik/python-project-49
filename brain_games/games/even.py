from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_data():
    start = 1
    end = 10
    question = randint(start, end)
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
