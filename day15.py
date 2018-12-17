import queue
import math
import numpy as np

start_points = 200 
attack = 3




def neighbours(maze, pos):
    ret = []
    if pos[0] > 0:
        ret.append((pos[0] - 1, pos[1]))
    if pos[0] < maze.shape[0] - 1:
        ret.append((pos[0] + 1, pos[1]))
    if pos[1] > 0:
        ret.append((pos[0], pos[1] - 1))
    if pos[1] < maze.shape[1] - 1:
        ret.append((pos[0], pos[1] + 1))

    return ret

def pos_comp(potential, current):
    return (potential[0] < current[0]) or (potential[0] == current[0] and potential[1] < current[1])

def closest(array, players, letter):
    shape = array.shape

    # closest contains (distance, source pos)
    closest = np.zeros(shape, dtype=object)

    for key, value in players.items():
        if value[0] == letter:
            closest[key] = [0,key]

    changed = True
    while changed:
        changed = False
        for y in range(shape[0]):
            for x in range(shape[1]):
                if closest[(y,x)] != 0:
                    src = closest[(y,x)]
                    for n in neighbours(array, (y,x)):
                        if array[n] == '.' and (closest[n] == 0 or closest[n][0] > src[0] + 1 or (closest[n][0] == src[0] + 1 and pos_comp(src[1], closest[n][1]))):
                            closest[n] = src[:]
                            closest[n][0] += 1
                            changed = True

    print(closest)
    exit(0)






def prepare(array):
    players = {}
    shape = array.shape

    for y in range(shape[0]):
        for x in range(shape[1]):
            if array[(y,x)] == 'G':
                players[(y,x)] = ['G', start_points]
            if array[(y,x)] == 'E':
                players[(y,x)] = ['E', start_points]

    return players

def adv(p):
    if p == 'E':
        return 'G'
    elif p == 'G':
        return 'E'

def main():
    file = open("inputs/input15.txt")

    lines = [x.rstrip() for x in file]

    size_x = max([len(l) for l in lines])
    size_y = len(lines)

    for y in range(size_y):
        lines[y] = lines[y] + ' ' * (size_x - len(lines[y]))
        lines[y] = list(lines[y])

    array = np.array(lines)

    players = prepare(array)

    while True:
        to_move = []
        for y in range(size_y):
            for x in range(size_x):
                if array[(y,x)] == 'E' or array[(y,x)] == 'G':
                    to_move.append((y,x))

        for pos in to_move:
            closest(array, players, adv(array[pos]))


            neigh = neighbours()

            for n in neigh:
                if array[n] == adv(array[pos]):
                    pass

     


 


main()
