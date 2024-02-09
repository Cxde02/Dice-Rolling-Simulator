import random

def face1():
    return [' -------',
            '|       |',
            '|   *   |',
            '|       |',
            ' -------']

def face2():
    return [' -------',
            '|*      |',
            '|       |',
            '|      *|',
            ' -------']

def face3():
    return [' -------',
            '|*      |',
            '|   *   |',
            '|      *|',
            ' -------']

def face4():
    return [' -------',
            '|*     *|',
            '|       |',
            '|*     *|',
            ' -------']

def face5():
    return [' -------',
            '|*     *|',
            '|   *   |',
            '|*     *|',
            ' -------']

def face6():
    return [' -------',
            '|*  *  *|',
            '|       |',
            '|*  *  *|',
            ' -------']

def roll_Dice1():
    print('Dice 1: ')
    # Randomly choose and print one of the faces
    random_face = random.choice([face1, face2, face3, face4, face5, face6])
    for line in random_face():
        print(line)

    if random_face == face1:
        print('You got 1')
        return 1
    elif random_face == face2:
        print('You got 2')
        return 2
    elif random_face == face3:
        print('You got 3')
        return 3
    elif random_face == face4:
        print('You got 4')
        return 4
    elif random_face == face5:
        print('You got 5')
        return 5
    else:
        print('You got 6')
        return 6

def roll_Dice2():
    print()
    print('Dice 2: ')
    # Randomly choose and print one of the faces
    random_face = random.choice([face1, face2, face3, face4, face5, face6])
    for line in random_face():
        print(line)

    if random_face == face1:
        print('You got 1')
        return 1
    elif random_face == face2:
        print('You got 2')
        return 2
    elif random_face == face3:
        print('You got 3')
        return 3
    elif random_face == face4:
        print('You got 4')
        return 4
    elif random_face == face5:
        print('You got 5')
        return 5
    else:
        print('You got 6')
        return 6

def sum_Of_Die():
    dice1 = roll_Dice1()
    dice2 = roll_Dice2()
    total = dice1 + dice2
    return f"{dice1} + {dice2} = {total}"


while True:
    print('\n---Dice Rolling Simulator---')
    print("Enter 'r' to Roll Dice or 'q' to Quit: ", end='')
    userInput = input().lower()
    if userInput == "r":
        result = sum_Of_Die()
        print('--------------------------')
        print("Sum of the dice:", result)
    elif userInput == "q":
        print('Exiting the program...')
        break
    else:
        print('System accepts only \'r\' and \'q\'')
