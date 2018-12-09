import queue
import math
import numpy as np

def main():
    infile = open("inputs/input9.txt")
    line = infile.readline()
    line = line.strip().split()

    nb_players, last = int(line[0]), int(line[6])

    player = 0
    marbles = [0]
    curr_pos = 0
    next_marble = 1
    scores = [0 for i in range(nb_players)]

    while next_marble <= last:
        pos = (curr_pos + 2) % len(marbles)

        if next_marble % 23:
            marbles = marbles[0:pos] + [next_marble] + marbles[pos:]
            curr_pos = pos
            next_marble += 1
        else:
            pos = (curr_pos + len(marbles) - 7) % len(marbles)
            scores[player] += next_marble + marbles[pos]
            marbles = marbles[0:pos] + marbles[pos+1:]
            curr_pos = pos % len(marbles)
            next_marble += 1

        #print("[{}] [{} {}] {}".format(player + 1, pos, marbles[pos], marbles))

        player = (player + 1) % nb_players

    print(max(scores))



if __name__ == "__main__":
    main()
