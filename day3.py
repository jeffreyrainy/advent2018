import queue
import math
import numpy as np
import string
import re

def main():
    file = open("inputs/input3.txt")

    # this will be inefficient, but hey, let's start simple

    # fabric usage per coordinate
    fabric = {}
    
    # ids of piece contributing to each coordinate
    ids = {}

    # ids of piece that overlap
    overlaps = set()

    for line in file:
        # read lines
        line = line.strip()
        line = line.replace('x',' ')
        line = re.findall(r"[\w']+", line)
        [id, pos_x, pos_y, size_x, size_y] = [int(x) for x in line]

        overlap = False

        # process each piece (we could use a data structure to speed this up, if we needed to)
        for x in range(size_x):
            for y in range(size_y):
                if (x + pos_x, y + pos_y) in fabric:
                    fabric[(x + pos_x, y + pos_y)] += 1
                    ids[(x + pos_x, y + pos_y)].add(id)
                    overlap = True
                    overlaps = overlaps.union(ids[(x + pos_x, y + pos_y)])
                else:
                    fabric[(x + pos_x, y + pos_y)] = 1
                    ids[(x + pos_x, y + pos_y)] = set()
                    ids[(x + pos_x, y + pos_y)].add(id)

    count = 0
    for key, value in fabric.items():
        if value>1:
            count += 1

    print("ovelap area is {}".format(count))

    for i in range(1,id):
        if not i in overlaps:
            print("{} doesn't overlap".format(i))
    

if __name__ == "__main__":
    main()
