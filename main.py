from random2 import randrange

# Code creates a guessing game where the computer guesses a number and gives the user hints. Can produce any number between 1  - 100 and returns a high score of 100.

# Definitions

random_number = randrange(1,101)
compare_number = randrange(2,11)
score = 100
print_score = ('Score = ' + str(score))
hint_generator_1 = randrange(1,4)
hint_generator_2 = randrange(1,4)
hint_generator_3 = randrange(1,4)
hint_generator_4 = randrange(1,4)
hint_generator_5 = randrange(1,4)
hint_generator_6 = randrange(1,4)
hint_generator_7 = randrange(1,4)
hint_generator_8 = randrange(1,4)
hint_generator_9 = randrange(1,4)
hint_generator_10 = randrange(1,4)

# functions for hints. A random type of hint will be given for each wrong answer.

def higher_or_lower_1(input_1, random_number):
    if input_1 > random_number:
        print('Guess lower')
    if input_1 < random_number:
        print('Guess higher')

def higher_or_lower_2(input_2, random_number):
    if input_2 > random_number:
        print('Guess lower')
    if input_2 < random_number:
        print('Guess higher')

def higher_or_lower_3(input_3, random_number):
    if input_3 > random_number:
        print('Guess lower')
    if input_3 < random_number:
        print('Guess higher')

def higher_or_lower_4(input_4, random_number):
    if input_4 > random_number:
        print('Guess lower')
    if input_4 < random_number:
        print('Guess higher')

def higher_or_lower_5(input_5, random_number):
    if input_5 > random_number:
        print('Guess lower')
    if input_5 < random_number:
        print('Guess higher')

def higher_or_lower_6(input_6, random_number):
    if input_6 > random_number:
        print('Guess lower')
    if input_6 < random_number:
        print('Guess higher')

def higher_or_lower_7(input_7, random_number):
    if input_7 > random_number:
        print('Guess lower')
    if input_7 < random_number:
        print('Guess higher')

def higher_or_lower_8(input_8, random_number):
    if input_8 > random_number:
        print('Guess lower')
    if input_8 < random_number:
        print('Guess higher')

def higher_or_lower_9(input_9, random_number):
    if input_9 > random_number:
        print('Guess lower')
    if input_9 < random_number:
        print('Guess higher')

def higher_or_lower_10(input_10, random_number):
    if input_10 > random_number:
        print('Guess lower')
    if input_10 < random_number:
        print('Guess higher')

def starts_with(random_number):
    first = int(str(random_number)[:1])
    print ('Your number starts with ' + str(first))

def divisable_by (random_number, compare_number):
    if random_number % compare_number == 0:
        print ('Divisable by ' + str(compare_number))
    if random_number % compare_number != 0:
        print ('Not divisable by ' + str(compare_number))

# User interfaces

def guessing_game(random_number):
    score = 100
    input_1 = int(input('What number am I thinking of?'))

    if input_1 == random_number:
        print ('Good job!!')
        print ('Score = ' + str(score))
        return
    elif input_1 != random_number and hint_generator_1 == 1:
        print ('Try again!')
        higher_or_lower_1(input_1, random_number)
        score = score - 10
        print ('Score = ' + str(score))
    elif input_1 != random_number and hint_generator_1 == 2:
        print ('Try again!')
        starts_with(random_number)
        score = score - 10
        print ('Score = ' + str(score))
    elif input_1 != random_number and hint_generator_1 == 3:
        print ('Try again!')
        divisable_by(random_number, compare_number)
        score = score - 10
        print ('Score = ' + str(score))
    else:
        print ('Something went wrong. Please try again!')

    input_2 = int(input('Guess Again'))

    if input_2 == random_number:
        print ('Good job!')
        print ('Score = ' + str(score))
        return
    elif input_2 != random_number and hint_generator_2 == 1:
        print('Try again!')
        higher_or_lower_2(input_2, random_number)
        score = score - 10
        print ('Score = ' + str(score))
    elif input_2 != random_number and hint_generator_2 == 2:
        print('Try again!')
        starts_with(random_number)
        score = score - 10
        print ('Score = ' + str(score))
    elif input_2 != random_number and hint_generator_2 == 3:
        print('Try again!')
        divisable_by(random_number, compare_number)
        score = score - 10
        print ('Score = ' + str(score))
    else:
        print('Something went wrong. Please try again!')

    input_3 = int(input('Guess Again'))

    if input_3 == random_number:
        print ('Good job!')
        print ('Score = ' + str(score))
        return
    elif input_3 != random_number and hint_generator_3 == 1:
        print('Try again!')
        higher_or_lower_3(input_3, random_number)
        score = score - 10
        print ('Score = ' + str(score))
    elif input_3 != random_number and hint_generator_3 == 2:
        print('Try again!')
        starts_with(random_number)
        score = score - 10
        print ('Score = ' + str(score))
    elif input_3 != random_number and hint_generator_3 == 3:
        print('Try again!')
        divisable_by(random_number, compare_number)
        score = score - 10
        print ('Score = ' + str(score))
    else:
        print('Something went wrong. Please try again!')

    input_4 = int(input('Guess Again'))

    if input_4 == random_number:
        print ('Good job!')
        print ('Score = ' + str(score))
        return
    elif input_4 != random_number and hint_generator_4 == 1:
        print('Try again!')
        higher_or_lower_4(input_4, random_number)
        score = score - 10
        print ('Score = ' + str(score))
    elif input_4 != random_number and hint_generator_4 == 2:
        print('Try again!')
        starts_with(random_number)
        score = score - 10
        print ('Score = ' + str(score))
    elif input_4 != random_number and hint_generator_4 == 3:
        print('Try again!')
        divisable_by(random_number, compare_number)
        score = score - 10
        print ('Score = ' + str(score))
    else:
        print('Something went wrong. Please try again!')

    input_5 = int(input('Guess Again'))

    if input_5 == random_number:
        print('Good job!')
        print('Score = ' + str(score))
        return
    elif input_5 != random_number and hint_generator_5 == 1:
        print('Try again!')
        higher_or_lower_5(input_5, random_number)
        score = score - 10
        print('Score = ' + str(score))
    elif input_5 != random_number and hint_generator_5 == 2:
        print('Try again!')
        starts_with(random_number)
        score = score - 10
        print('Score = ' + str(score))
    elif input_5 != random_number and hint_generator_5 == 3:
        print('Try again!')
        divisable_by(random_number, compare_number)
        score = score - 10
        print('Score = ' + str(score))
    else:
        print('Something went wrong. Please try again!')

    input_6 = int(input('Guess Again'))

    if input_6 == random_number:
        print('Good job!')
        print('Score = ' + str(score))
        return
    elif input_6 != random_number and hint_generator_6 == 1:
        print('Try again!')
        higher_or_lower_6(input_6, random_number)
        score = score - 10
        print('Score = ' + str(score))
    elif input_6 != random_number and hint_generator_6 == 2:
        print('Try again!')
        starts_with(random_number)
        score = score - 10
        print('Score = ' + str(score))
    elif input_6 != random_number and hint_generator_6 == 3:
        print('Try again!')
        divisable_by(random_number, compare_number)
        score = score - 10
        print('Score = ' + str(score))
    else:
        print('Something went wrong. Please try again!')

    input_7 = int(input('Guess Again'))

    if input_7 == random_number:
        print('Good job!')
        print('Score = ' + str(score))
        return
    elif input_7 != random_number and hint_generator_7 == 1:
        print('Try again!')
        higher_or_lower_7(input_7, random_number)
        score = score - 10
        print('Score = ' + str(score))
    elif input_7 != random_number and hint_generator_7 == 2:
        print('Try again!')
        starts_with(random_number)
        score = score - 10
        print('Score = ' + str(score))
    elif input_7 != random_number and hint_generator_7 == 3:
        print('Try again!')
        divisable_by(random_number, compare_number)
        score = score - 10
        print('Score = ' + str(score))
    else:
        print('Something went wrong. Please try again!')

    input_8 = int(input('Guess Again'))

    if input_8 == random_number:
        print('Good job!')
        print('Score = ' + str(score))
        return
    elif input_8 != random_number and hint_generator_8 == 1:
        print('Try again!')
        higher_or_lower_8(input_8, random_number)
        score = score - 10
        print('Score = ' + str(score))
    elif input_8 != random_number and hint_generator_8 == 2:
        print('Try again!')
        starts_with(random_number)
        score = score - 10
        print('Score = ' + str(score))
    elif input_8 != random_number and hint_generator_8 == 3:
        print('Try again!')
        divisable_by(random_number, compare_number)
        score = score - 10
        print('Score = ' + str(score))
    else:
        print('Something went wrong. Please try again!')

    input_9 = int(input('Guess Again'))

    if input_9 == random_number:
        print('Good job!')
        print('Score = ' + str(score))
        return
    elif input_9 != random_number and hint_generator_9 == 1:
        print('Try again!')
        higher_or_lower_9(input_9, random_number)
        score = score - 10
        print('Score = ' + str(score))
    elif input_9 != random_number and hint_generator_9 == 2:
        print('Try again!')
        starts_with(random_number)
        score = score - 10
        print('Score = ' + str(score))
    elif input_9 != random_number and hint_generator_9 == 3:
        print('Try again!')
        divisable_by(random_number, compare_number)
        score = score - 10
        print('Score = ' + str(score))
    else:
        print('Something went wrong. Please try again!')

    input_10 = int(input('Guess Again'))

    if input_10 == random_number:
        print('Good job!')
        print('Score = ' + str(score))
        return
    else:
        print('Game Over!')
        return

guessing_game(random_number)