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

print('---Dice Rolling Simulator---')

# Randomly choose and print one of the faces
random_face = random.choice([face1, face2, face3, face4, face5, face6])
for line in random_face():
    print(line)

if random_face == face1:
    print('You got 1')
elif random_face == face2:
    print('You got 2')
elif random_face == face3:
    print('You got 3')
elif random_face == face4:
    print('You got 4')
elif random_face == face5:
    print('You got 5')
else:
    print('You got 6')
