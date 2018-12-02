import queue
import math
import numpy as np

def main():
    file = open("inputs/input2.txt")

    twos = 0
    threes = 0
    for line in file:
        line = line.strip()
        line = [x for x in line]
        line.sort()
        line.append('.')

        running = 1
        two = False
        three = False
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                running += 1
            else:
                if running == 2:
                    two = True
                if running == 3:
                    three = True
                running = 1

        if two:
            twos += 1
        if three:
            threes += 1

    print(twos, threes, twos * threes)

if __name__ == "__main__":
    main()
