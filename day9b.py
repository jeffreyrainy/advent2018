import queue
import math
import numpy as np
from collections import deque

left_marbles = deque()
right_marbles = deque()

curr_pos = 0
right_marbles.append(0)

def balance():
    if len(right_marbles) == 0:
        for i in range((len(left_marbles) + 1) // 2):
            right_marbles.append(left_marbles.popleft())
    elif len(left_marbles) == 0:
        for i in range((len(right_marbles) + 1) // 2):
            left_marbles.appendleft(right_marbles.pop()) 

def right(n):
    for i in range(n):
        if len(right_marbles) == 0:
            balance()
        left_marbles.append(right_marbles.popleft())

def left(n):
    for i in range(n):
        if len(left_marbles) == 0:
            balance()
        right_marbles.appendleft(left_marbles.pop())

def remove():

    if len(right_marbles) == 0:
        balance()
    return right_marbles.popleft()

def marble_string():
    ret = ""
    l = len(left_marbles)
    for i in range(l):
        value = left_marbles.popleft()
        ret += str(value) + " "
        left_marbles.append(value)

    l = len(right_marbles)
    for i in range(l):
        value = right_marbles.popleft()
        if i == 0:
            ret += "(" + str(value) + ") "
        else:
            ret += str(value) + " "
        right_marbles.append(value)

    return ret

def insert(value):
    right_marbles.appendleft(value)

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
