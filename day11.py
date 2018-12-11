import queue
import math
import numpy as np
import copy

# this could be massively improved.
# but it gave the answer fast enough.
def process(values, r):
    best = 0
    best_coord = None
    for z in range(r[0], r[1]):
        for x in range(300 - (z-1)):
            for y in range(300 - (z-1)):
                v = np.sum(values[x:x+z,y:y+z])
                if v > best:
                    best = v
                    best_coord = (x,y,z)

    print(best_coord)

def main():
    file = open("inputs/input11.txt")

    serial = int(file.readline())
    print(serial)

    values = np.zeros((300,300))

    for x in range(300):
        for y in range(300):
            v = ((x + 10) * y + serial) * (x + 10)
            values[(x,y)] = (v // 100) % 10 - 5

    process(values, [3, 4])
    process(values, [0, 300])

if __name__ == "__main__":
    main()
