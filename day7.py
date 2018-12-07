import queue
import math
import numpy as np

def main():
    file = open("inputs/input7.txt")

    prereq = {}

    for line in file:
        line = line.strip().split()
        a, b = line[1], line[7]

        if not a in prereq:
            prereq[a] = []
        if not b in prereq:
            prereq[b] = []

        prereq[b].append(a)

    done = False
    while prereq and len(prereq) != 0:
        picked = None
        for k in sorted(prereq.keys()):
            v = prereq[k]
            if not v or len(v) == 0:
                picked = k
                break

        print(picked, end = "")
        del prereq[picked]

        for k,v in prereq.items():
            if v and picked in v:
                prereq[k].remove(picked)
        




if __name__ == "__main__":
    main()
