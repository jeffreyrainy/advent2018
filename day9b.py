import queue
import math
import numpy as np
from collections import deque

marbles = deque()

curr_pos = 0
marbles.append(0)

def right(n):
    for i in range(n):
        marbles.append(marbles.popleft())

def left(n):
    for i in range(n):
        marbles.appendleft(marbles.pop())

def remove():
    return marbles.popleft()

def marble_string():
    ret = ""

    l = len(marbles)
    for i in range(l):
        value = marbles.popleft()
        if i == 0:
            ret += "(" + str(value) + ") "
        else:
            ret += str(value) + " "
        marbles.append(value)

    return ret

def insert(value):
    marbles.appendleft(value)

def main():
    infile = open("inputs/input9.txt")
    line = infile.readline()
    line = line.strip().split()

    nb_players, last = int(line[0]), int(line[6])
    last = last * 100

    player = 0
    
    next_marble = 1
    scores = [0 for i in range(nb_players)]

    last_perthousand = 0

    while next_marble <= last:

        if next_marble % 23:
            right(2)
            insert(next_marble)
            next_marble += 1
        else:
            left(7)
            scores[player] += next_marble + remove()
            next_marble += 1

        #print("[{}] {}".format((player + 1), marble_string()))

        player = (player + 1) % nb_players

    print(max(scores))



if __name__ == "__main__":
    main()
